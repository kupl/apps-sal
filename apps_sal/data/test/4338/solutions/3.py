(n, x, y) = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()
if x > y:
    print(n)
else:
    k = sum([1 for i in b if i <= x])
    print((k + (k % 2 == 1)) // 2)
