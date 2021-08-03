n = int(input())
a = [0] * n
x = [0] * 100001

for i in range(n):
    s, a[i] = list(map(int, input().split()))
    x[s] += 1

for i in range(n):
    print(n - 1 + x[a[i]], n - 1 - x[a[i]])
