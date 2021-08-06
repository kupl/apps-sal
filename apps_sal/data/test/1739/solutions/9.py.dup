n, x = map(int, input().split())
t = list(map(int, input().split()))
b = max(t)
k = t.count(b)
r = sum(t)
s = r - b
while k % x == 0:
    b -= 1
    s += 1
    k = k // x + t.count(b)
print(pow(x, min(r, s), 1000000007))
