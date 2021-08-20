n = int(input())
a = list(map(int, input().split())) + [0]
b = [abs(a[0])] + [abs(a[i + 1] - a[i]) for i in range(n)]
c = [abs(a[1])] + [abs(a[i + 2] - a[i]) for i in range(n - 1)]
hon = sum(b)
for i in range(n):
    print(hon - b[i] - b[i + 1] + c[i])
