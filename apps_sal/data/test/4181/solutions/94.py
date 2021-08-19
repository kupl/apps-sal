n = int(input())
a_l = list(map(int, input().split()))
b_l = list(map(int, input().split()))
ans = 0
c = 0
for i in range(1, n + 1):
    a = a_l[-i]
    if b_l[-i] + c >= a:
        ans += a
        d = c - a
        if d >= 0:
            d = 0
        c = b_l[-i] - abs(d)
    else:
        ans += b_l[-i] + c
        c = 0
if a_l[0] >= c:
    ans += c
else:
    ans += a_l[0]
print(ans)
