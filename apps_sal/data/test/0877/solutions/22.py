(n, m) = list(map(int, input().split()))
div1 = []
div2 = []
i = 0
ans = -5
while i < m:
    (a, b) = list(map(int, input().split()))
    div1.append(max(a, b))
    div2.append(min(a, b))
    i += 1
if m == 0:
    print(n - 1)
else:
    ans = min(div1) - max(div2)
    if ans <= 0:
        print(0)
    else:
        print(ans)
