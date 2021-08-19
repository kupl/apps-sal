(n, a, b) = list(map(int, input().split()))
n10 = a
n20 = b
n21 = 0
t = list(map(int, input().split()))
ans = 0
for i in t:
    if i == 1:
        if n10:
            n10 -= 1
        elif n20:
            n20 -= 1
            n21 += 1
        elif n21:
            n21 -= 1
        else:
            ans += 1
    elif n20:
        n20 -= 1
    else:
        ans += 2
print(ans)
