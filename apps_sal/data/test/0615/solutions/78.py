N = int(input())
As = list(map(int, input().split()))
sum_a = [0]
for i in range(N):
    sum_a.append(As[i] + sum_a[i])
ans = float('inf')
(p, q) = (0, 2)
for cut in range(2, N - 1):
    while p < cut - 1:
        if abs(sum_a[cut] - sum_a[p] * 2) >= abs(sum_a[cut] - sum_a[p + 1] * 2):
            p += 1
        else:
            break
    while q < N - 1:
        if abs(sum_a[N] - sum_a[q] - (sum_a[q] - sum_a[cut])) >= abs(sum_a[N] - sum_a[q + 1] - (sum_a[q + 1] - sum_a[cut])):
            q += 1
        else:
            break
    ls = [sum_a[N] - sum_a[q], sum_a[q] - sum_a[cut], sum_a[cut] - sum_a[p], sum_a[p]]
    ans = min(ans, max(ls) - min(ls))
print(ans)
