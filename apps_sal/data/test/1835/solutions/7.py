def sv():
    N = int(input())
    tot0 = 0
    allEven = True
    for n in range(N):
        s = input()
        if len(s) % 2: allEven = False
        tot0 += sum(1 for c in s if c == '0')
    print((N - 1) if allEven and tot0 % 2 else N)


TC = int(input())
for tc in range(TC):
    sv()
