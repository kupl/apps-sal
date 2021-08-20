(n, battery, accumulator) = list(map(int, input().split()))
s = list(map(int, input().split()))
b = battery
a = accumulator
ans = 0
for i in range(n):
    if a == 0 and b == 0:
        break
    elif s[i] == 0:
        if a > 0:
            a -= 1
            ans += 1
        else:
            b -= 1
            ans += 1
    elif a == accumulator:
        a -= 1
        ans += 1
    elif b > 0:
        b -= 1
        a += 1
        ans += 1
    else:
        a -= 1
        ans += 1
print(ans)
