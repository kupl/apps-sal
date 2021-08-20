(n, d) = list(map(int, input().split()))
a = list(map(int, input().split()))
m = int(input())
if m > n:
    print(sum(a) - (m - n) * d)
else:
    a.sort()
    print(sum(a[0:m]))
