s = input()
k = int(input())
for i in range(k):
    if s[i] != '1':
        ans = s[i]
        break
    elif i < k - 1:
        ans = s[i + 1]
    else:
        ans = s[i]

print(ans)
