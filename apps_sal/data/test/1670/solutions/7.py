
name1 = input()
name2 = input()
faults = int(input())

s1 = [0] * 100
s2 = [0] * 100

for i in range(faults):
    time, t, m, card = input().split()
    time = int(time)
    m = int(m)
    s = s1 if t == 'h' else s2

    if card == 'y':
        if s[m] == 1:
            print(name1 if t == 'h' else name2, m, time)
        s[m] += 1
    elif s[m] < 2:
        print(name1 if t == 'h' else name2, m, time)
        s[m] += 2
