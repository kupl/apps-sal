s = input()
k = int(input())
ans = 1
for i in range(min(k, len(s))):
    if s[i] != '1':
        ans = int(s[i])
        break
print(ans)
