a, b = map(int, input().split())
k = 0
l = 0
s = 0
for i in range(1, 7):
    if abs(a - i) > abs(b - i):
        k += 1
    elif abs(a - i) == abs(b - i):
        l += 1
    else:
        s += 1

print(s, l, k)
