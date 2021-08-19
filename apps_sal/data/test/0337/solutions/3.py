(w, h) = list(map(int, input().split()))
(w1, d1) = list(map(int, input().split()))
(w2, d2) = list(map(int, input().split()))
ans = w
for i in reversed(list(range(h + 1))):
    ans += i
    if i == d1:
        ans = max(0, ans - w1)
    if i == d2:
        ans = max(0, ans - w2)
print(ans)
