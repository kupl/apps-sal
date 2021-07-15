ls =[]
ans = 'Yay!'
for i in range(5):
    ls.append(int(input()))
k = int(input())
for i in range(5):
    for j in range(5):
        if abs(ls[i]-ls[j]) > k:
            ans = ':('
            break
print(ans)
