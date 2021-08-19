s = list(map(int, input()))
k = int(input())
for i in range(k):
    if s[i] != 1:
        ans = s[i]
        break
    else:
        ans = 1
print(ans)
