a, b = list(map(int, input().split()))
res = 0

for i in range(2):
    if a >= b:
        res += a
        a -= 1
    else:
        res += b
        b -= 1

print(res)

