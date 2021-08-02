def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


N = int(input())
F = [int("".join(input().split()), 2) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]
ans = -float("inf")
for i in range(1, 1 << 10):
    tmp = 0
    for j in range(N):
        tmp += P[j][count_set_bits(i & F[j])]
    ans = max(ans, tmp)
print(ans)
