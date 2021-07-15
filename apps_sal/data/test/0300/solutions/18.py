n = int(input())
a = list(map(int, input().split()))

s = sum(a)
ans = 0
while 2 * s / n < 9:
    m = min(a)
    a.remove(m)
    a.append(5)
    s += 5 - m
    ans += 1

print(ans)

