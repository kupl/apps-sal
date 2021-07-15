n = int(input())
snacks = list(map(int, input().split()))
present = [0] * (n + 1)
exp = n
i = 0
for i in range(n):
    s = snacks[i]
    present[s] = 1
    curans = ''
    if s == exp:
        curans = str(exp) + ' '
        while exp - 1 > 0 and present[exp - 1]:
            curans += str(exp - 1) + ' '
            exp -= 1
        exp -= 1
    if curans:
        print(curans[:-1])
    else:
        print('')
