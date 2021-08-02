n = int(input())
s, t = map(str, input().split())
ans = ['0'] * n
for i in range(n):
    ans[i] = s[i] + t[i]
print(''.join(ans))
