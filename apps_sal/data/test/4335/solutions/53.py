N = int(input())
S = input()

ans = 'No'
# Nが偶数のときを考えればよい
if N % 2 == 0:
    if S[:N // 2] == S[N // 2:]: ans = 'Yes'

print(ans)
