def r():
    return map(int, input().split())


(n, m) = r()
s = 100000000000.0
for _ in range(n):
    (a, b) = r()
    s = min(s, a / b)
print(s * m)
