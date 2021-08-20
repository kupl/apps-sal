n = int(input())
a = list(map(int, input().split()))
(x1, x2) = (len([q for q in a if q > 0]), a.count(0))
x3 = n - x1 - x2
if x1 >= (n + 1) // 2:
    print(1)
elif x3 >= (n + 1) // 2:
    print(-1)
else:
    print(0)
