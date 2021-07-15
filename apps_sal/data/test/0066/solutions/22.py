t, w, b = list(map(int, input().split()))

def gcd(x, y):
    while (x != 0 and y != 0):
        if (x < y):
            x, y = y, x
        x %= y
    return x + y;

ans = (t // (w * b // gcd(w, b)) - 1) * min(w, b)
ans += min(t - (t // (w * b // gcd(w, b))) * (w * b // gcd(w, b)) + 1, min(b, w))
ans += min(w, b) - 1;
print(ans // gcd(ans, t), end = "/")
print(t // gcd(ans, t))
