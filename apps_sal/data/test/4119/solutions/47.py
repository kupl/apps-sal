N, M = list(map(int, input().split()))
if N > M:
    print((0))
    return
lst = list(map(int, input().split()))
lst.sort()
sum_1 = max(lst) - min(lst)
D = []
for i in range(1, M):
    D.append(lst[i] - lst[i - 1])
D.sort(reverse=True)
sum_2 = 0
for i in range(N - 1):
    sum_2 += D[i]
ans = 0
ans = sum_1 - sum_2
print(ans)
