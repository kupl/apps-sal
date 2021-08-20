n = int(input())
a = sorted(list(map(int, input().split())))
(ansA, ansB) = (0, 0)
for i in range(n // 2):
    (u, v) = (i * 2 + 1, i * 2 + 2)
    ansA += abs(a[i] - u)
    ansB += abs(a[i] - v)
print(min(ansA, ansB))
