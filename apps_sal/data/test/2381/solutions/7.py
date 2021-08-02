n, k = map(int, input().split())
a = [int(x) for x in input().split()]
mod = 10**9 + 7
nega = sorted([a[i] for i in range(n) if a[i] < 0], reverse=True)

v = []
if k == n:
    # 全掛け算
    v = a
elif k % 2 and n == len(nega):
    # 答えは負
    v = nega[:k]
else:
    # 答えは正
    a = sorted(a, key=lambda x: abs(x), reverse=True)
    pi = ni = -1; cnt = 0;
    for i in range(k):
        v.append(a[i])
        if a[i] < 0: ni = i; cnt += 1
        if a[i] > 0: pi = i;
    if cnt % 2:
        mx = max(a[k:]); mn = min(a[k:]);
        if pi >= 0 and abs(a[pi] * mx) <= abs(a[ni] * mn):
            v.append(mn); v.remove(a[pi]);
        else:
            v.append(mx); v.remove(a[ni]);

ans = 1
for i in range(k):
    ans *= v[i]; ans %= mod;

print(ans)
