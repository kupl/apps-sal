antenna = [int(input()) for _ in range(5)]
k = int(input())
ans = 'Yay!'
for i in range(5):
    for j in range(5):
        if i < j:
            if antenna[j] - antenna[i] > k:
                ans = ':('
                break
    else:
        continue
    break
print(ans)
