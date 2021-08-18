n, p = list(map(int, input().split()))
p -= 1
st = input().strip()
l = 0
h = n // 2 - 1
if p > h:
    p = n - 1 - p
inside = False
ans = 0
i = 0
H = -1
while i <= h:
    if st[i] != st[n - 1 - i]:
        if not inside:
            l = i
            inside = True
        H = i
    ans += min(abs(ord(st[i]) - ord(st[n - 1 - i])), abs(ord('z') - ord('a') + 1 - abs(ord(st[i]) - ord(st[n - 1 - i]))))
    i += 1
h = H
if h == -1:
    print("0")
    return
ans += h - l
ans += min(abs(l - p), abs(p - h))
print(ans)
