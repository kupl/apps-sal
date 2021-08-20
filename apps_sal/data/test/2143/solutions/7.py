n = int(input())
a = list(map(int, input().split()))
b = [0 for i in range(200005)]
if n == 2:
    print(1)
else:
    for i in range(n - 1):
        for j in range(i + 1, n):
            b[a[i] + a[j]] += 1
    print(max(b))
