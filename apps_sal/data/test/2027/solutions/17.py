n = int(input())
a = list(map(int, input().split()))
a.append(0)
for i in range(n):
    print(a[i] + a[i+1], end=' ')

