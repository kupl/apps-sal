n = int(input())
x = list(map(int, input().split()))
x2 = sorted(x)
mid = n // 2 - 1
for i in range(n):
    xi = x[i]
    if x2[mid] < xi:
        print((x2[mid]))
    else:
        print((x2[mid + 1]))
