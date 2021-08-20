from itertools import accumulate
n = int(input())
mas = list([0 for x in range(101)])
(x0, y0) = list(map(int, input().split()))
for i in range(n - 1):
    (x, y) = list(map(int, input().split()))
    mas[x] += 1
    mas[y] -= 1
ans = list(accumulate(mas))[x0:y0].count(0)
print(ans)
