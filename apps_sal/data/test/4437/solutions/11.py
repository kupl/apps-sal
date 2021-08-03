N = int(input())
S = list(input())
k = N // 2
ans = 0
T = ''
for i in range(k):
    if S[2 * i] == S[2 * i + 1]:
        ans += 1
        T += 'ab'
    else:
        T += S[2 * i] + S[2 * i + 1]
print(ans)
print(T)
