n = int(input())
let = list(map(int, input().split()))
inbox = 1
ans = 0
for l in let:
    if inbox == 1:
        if l == 1:
            ans += 1
            inbox = 0
    else:
        if l == 1:
            ans += 1
        else:
            ans += 1
            inbox = 1
if ans > 0 and let[n - 1] == 0:
    ans -= 1
print(ans)
