n = int(input())
a1, a2 = 0, 0
r = 0
for _ in range(n):
    b1, b2 = list(map(int, input().split()))
    a2 = max(0, a2 - (b1 - a1)) + b2
    r = max(r, a2)
    a1 = b1
print(a1 + a2, r)
