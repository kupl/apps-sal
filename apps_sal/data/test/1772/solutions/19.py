n = int(input())
a = list(map(int, input().split()))
k = 0
d = 0
for i in range(n):
    if a[i] % 2 == 1:
        k += 1
    else:
        d += 1
    if k < d:
        ma = k
    else:
        ma = d
while k > 2:
    k -= 2
    d += 1
    if k < d:
        if k > ma:
            ma = k
    elif d > ma:
        ma = d
print(ma)
