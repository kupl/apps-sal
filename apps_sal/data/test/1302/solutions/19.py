n, k = map(int, input().split(" "))
if k >= n:
    print("-1")
elif n - 1 == k:
    for i in range(1, n + 1):
        print(i, end=" ")
else:
    a = [k + 2] + list(range(2, k + 2)) + list(range(k + 3, n + 1)) + [1]
    print(*a)
