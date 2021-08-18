inf = float('inf')

N = int(input())
a = tuple(map(int, input().split()))

c_sum = [0]
t = 0
for aa in a:
    t += aa
    c_sum.append(t)

ans = inf
p, q = 0, 2
for cut in range(2, N - 2 + 1):

    while p < cut - 1:
        if abs(c_sum[cut] - c_sum[p] * 2) >= abs(c_sum[cut] - c_sum[p + 1] * 2):
            p += 1
        else:
            break

    while q < N - 1:
        if abs(c_sum[N] - c_sum[q] - (c_sum[q] - c_sum[cut])) >= abs(
                c_sum[N] - c_sum[q + 1] - (c_sum[q + 1] - c_sum[cut])):
            q += 1
        else:
            break

    cands = [c_sum[cut] - c_sum[p], c_sum[p], c_sum[N] - c_sum[q], c_sum[q] - c_sum[cut]]
    ans = min(ans, max(cands) - min(cands))
print(ans)
