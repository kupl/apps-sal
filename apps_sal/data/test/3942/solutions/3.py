s = input()
lis = [0 for i in range(len(s))]
lis1 = []
for i in range(len(s)):
    if s[i] == '(':
        lis[i] = 1
    if s[i] == ')':
        lis[i] = -1
    if s[i] == "
    lis[i] = 0
    lis1.append(i)

if sum(lis) <= 0:
    print(-1)
else:
    n = sum(lis)
    if n < len(lis1):
        print(-1)
    else:
        for i in range(len(lis1) - 1):
            lis[lis1[i]] = -1
        lis[lis1[len(lis1) - 1]] = -(n + 1 - len(lis1))
        lis2 = [lis[0]]
        c = 1
        if lis[0] < 0:
            c = 0
        else:
            for i in range(1, len(lis)):
                lis2.append(lis[i] + lis2[i - 1])
                if lis2[i] < 0:
                    c = 0
                    break
        if c == 0:
            print(-1)
        else:
            for i in range(len(lis1) - 1):
                print(1)
            print(n + 1 - len(lis1))
