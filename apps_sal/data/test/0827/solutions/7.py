N = int(input())
T = input()
S = '110' * N
ans = 0
for i in range(3):
    if S[i:i + N] == T:
        ans += 10 ** 10 + -(i + N) // 3 + 1
print(ans)
