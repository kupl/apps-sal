n = int(input())

mn = mx = cur = 0
s = set()
for i in range(n):
    cmd = input()
    if cmd[0] == '+':
        s.add(int(cmd[2:]))
        cur += 1
        mx = max(mx, cur)
    else:
        cur -= 1
        try:
            s.remove(int(cmd[2:]))
        except KeyError:
            mn -= 1
print(mx - mn)

