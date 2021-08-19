(n, m, c) = map(int, input().split())
list01 = list(map(int, input().split()))
a = 0
b = 0
for i in range(n):
    list02 = list(map(int, input().split()))
    for j in range(m):
        a += list02[j] * list01[j]
    if a + c > 0:
        b += 1
        a = 0
    else:
        a = 0
print(b)
