n = int(input())
T = input()
S = '110' * 10 ** 5
ans = 0
l = 10 ** 10
for i in range(3):
    if S[i:i + len(T)] == T:
        ans += l - (n + i - 1) // 3
print(ans)
