(n, m, c) = map(int, input().split())
co = 0
b = list(map(int, input().split()))
for i in range(n):
    a = list(map(int, input().split()))
    s = 0
    for i in range(len(a)):
        s += a[i] * b[i]
    res = s + c
    if res > 0:
        co += 1
print(co)
