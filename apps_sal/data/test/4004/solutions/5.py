input()
n = list({int(x) for x in input().split()})
if len(n) == 1:
    print('0')
elif len(n) > 3:
    print('-1')
elif len(n) == 2:
    if abs(n[0] - n[1]) % 2 == 0:
        print(abs(n[0] - n[1]) // 2)
    else:
        print(abs(n[0] - n[1]))
else:
    n = sorted(n)
    if n[2] - n[1] == n[1] - n[0]:
        print(n[2] - n[1])
    else:
        print('-1')
