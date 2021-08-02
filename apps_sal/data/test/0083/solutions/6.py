n = int(input())
cl = list(map(int, input().split()))
a = 0
b = 0
for x in cl:
    if x > 0:
        a += 1
    if x < 0:
        b += 1

if n % 2 == 0:
    k = n // 2
else:
    k = n // 2 + 1

if a >= k:
    print(1)
elif b >= k:
    print(-1)
else:
    print(0)
