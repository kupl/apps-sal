(n, m) = map(int, input().split())
arr = list(map(int, input().split()))
s = 0
for i in arr:
    s += i
    print(s // m, end=' ')
    s = s % m
