n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
q = list(map(int, input().split()))

x = sum(a)

for i in range(m):
    print(x - a[n - q[i]])
