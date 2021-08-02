a = list(map(int, input().split()))
b = list(map(int, input().split()))
a1 = min(a[0::2])
b1 = max(a[0::2])
c1 = min(a[1::2])
d1 = max(a[1::2])
g = sum(b[0::2]) / 4
h = sum(b[1::2]) / 4
r = abs(b[0] - g) + abs(b[1] - h)
for i in range(a1, b1 + 1):
    for j in range(c1, d1 + 1):
        if abs(i - g) + abs(j - h) <= r:
            print("YES"); return
print("NO")
