n = int(input())
s = input()
t = ''
for ss in s:
    t += ss
    if len(t) >= 3:
        if t[len(t) - 3:len(t)] == 'fox':
            t = t[:len(t) - 3]
print(len(t))
