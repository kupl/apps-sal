s = input()
N = len(s)
ans = N // 2
for i in range(N):
    if(s[i] == 'p'):
        ans -= 1
print(ans)
