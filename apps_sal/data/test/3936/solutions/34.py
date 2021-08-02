n = int(input())
s1 = input()
s2 = input()

domino = []
i = 0
while i < n:
    if s1[i] == s2[i]:
        domino.append('X')
        i += 1
    else:
        domino.append('Y')
        i += 2

cnt = 0
if domino[0] == 'X':
    cnt += 3
else:
    cnt += 6

if len(domino) == 1:
    print(cnt % (10**9 + 7))
else:
    for i in range(1, len(domino)):
        if domino[i] == 'X':
            if domino[i - 1] == 'X':
                cnt *= 2
            else:
                cnt *= 1
        else:
            if domino[i - 1] == 'X':
                cnt *= 2
            else:
                cnt *= 3
    print(cnt % (10**9 + 7))
