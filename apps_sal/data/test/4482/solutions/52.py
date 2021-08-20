N = int(input())
l = list(map(int, input().split()))
cal = []
for i in range(-100, 101):
    a = 0
    for j in l:
        a += (i - j) ** 2
    cal.append(a)
ans = min(cal)
print(ans)
