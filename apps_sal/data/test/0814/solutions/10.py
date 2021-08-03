a = []
n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
for i in range(n):
    print(a[i], end=' ')
