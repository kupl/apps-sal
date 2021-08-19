S = str(input())
N = len(S)
ans = 0
for i in range(1, N, 2):
    ans += 9 * 10 ** (i - 1)
if N % 2 != 0:
    ans += int(S) - 10 ** (N - 1) + 1
print(ans)
