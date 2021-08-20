n = int(input())
s = input()
balance = 0
i = 0
calc = [1] * n
(firstr, lastl) = (-1, -1)
while i < n:
    if s[i] == 'R':
        balance += 1
        if firstr == -1:
            firstr = i
        i += 1
    elif s[i] == 'L':
        balance -= 1
        lastl = i
        i += 1
    else:
        i += 1
        continue
    if balance == 0:
        if (firstr - lastl) % 2 == 0:
            for j in range(firstr, lastl + 1):
                calc[j] = 0
            calc[(firstr + lastl) // 2] = 1
        else:
            for j in range(firstr, lastl + 1):
                calc[j] = 0
        firstr = -1
        lastl = -1
    elif balance == -1:
        calc = [0] * i + calc[i:]
        balance = 0
if balance != 0:
    calc = calc[:firstr] + [0] * (n - firstr)
print(sum(calc))
