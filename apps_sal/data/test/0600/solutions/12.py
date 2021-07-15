x1 = int(input())
x2 = int(input())
ust = 1
ans = 0
s = abs(x2 - x1)
while s > 1:
    s -= 2
    ans += ust * 2
    ust += 1
if s == 1:
    ans += ust
print(ans)
