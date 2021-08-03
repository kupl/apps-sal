w, m, k = map(int, input().split())
ans = 0

while w > 0:
    l = len(str(m))
    ans += min(w / (l * k), (10 ** l - m))
    w -= k * (10 ** l - m) * l
    m = 10 ** l
print(int(ans))
