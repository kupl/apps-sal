def gcd(a, b):
    while (b):
        a %= b
        a, b = b, a
    return a;


t, w, b = map(int, input().split())
g = w * b // gcd(w, b)
res = 0
minh = min(w, b)
res += (t // g + 1) * minh - 1
correct = (t // g) * g + minh - 1
if (correct > t):
    res -= correct - t
y = gcd(res, t)
print(res // y, "/", t // y, sep="")
