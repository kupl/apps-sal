s1 = list(map(int, input().split()))
s = list(map(int, input().split()))
h, n = s1[0], s1[1]
hp = h
time = 0
mins = 0
sums = 0
for i in range(n):
    sums += s[i]
    mins = min(mins, sums)
while time != n:
    hp = hp + s[time]
    time += 1
    if hp <= 0:
        break
if hp <= 0:
    print(time)
else:
    t = sum(s)
    if t >= 0:
        print(-1)
    else:
        hp1 = h + mins
        cycle = hp1 // abs(t)
        time = n * (hp1 // abs(t))
        timemod = 0
        hp = h - abs(t) * cycle
        while hp > 0:
            hp += s[timemod]
            timemod = (timemod + 1) % n
            time += 1
        print(time)
