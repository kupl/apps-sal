N, A, B = map(int, input().split())

if (A + B > N + 1) or (A * B < N):
    print(-1)
    return


distributes = [1] * A
remain = N - A
for i in range(A):
    d = min(remain, B - 1)
    distributes[i] += d
    remain -= d

marker = 1
ans = []
for d in distributes:
    ans.extend(list(range(marker, marker + d))[::-1])
    marker += d
print(*ans, sep=' ')

