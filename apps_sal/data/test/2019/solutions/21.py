t = int(input())
while t > 0:
    s = input()
    s0 = s.count('0')
    s1 = s.count('1')
    mini = min(s0, s1)
    if mini % 2 == 0:
        print('NET')
    else:
        print('DA')
    t -= 1
