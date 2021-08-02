N = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'

ans = ''
while 26 < N:
    s = (N - 1) % 26
    ans = alpha[s] + ans
    N = int(N - 1) // 26
ans = alpha[N - 1] + ans
print(ans)
