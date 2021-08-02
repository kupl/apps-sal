n, m = list(map(int, input().split()))
p = [input().split() for _ in range(m)]
ac = [0] * n
wa = [0] * n
for i in p:
    if i[1] == "AC" and ac[int(i[0]) - 1] == 0:
        ac[int(i[0]) - 1] = 1
    elif i[1] == "WA" and ac[int(i[0]) - 1] == 0:
        wa[int(i[0]) - 1] += 1
wasum = 0
for i in range(n):
    if ac[i] == 1:
        wasum += wa[i]
print(f"{sum(ac)} {wasum}")
