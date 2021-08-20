import sys
input = sys.stdin.readline


def ins():
    return input().rstrip()


def ini():
    return int(input().rstrip())


def inm():
    return map(int, input().rstrip().split())


def inl():
    return list(map(int, input().split()))


out = lambda x, s='\n': print(s.join(map(str, x)))
a = inl()
b = inl()
c = inl()
n = ini()
bingo = []
for _ in range(n):
    bingo.append(ini())
ct = [0] * 9
for i in bingo:
    if i in a:
        ct[a.index(i)] = 1
    if i in b:
        ct[b.index(i) + 3] = 1
    if i in c:
        ct[c.index(i) + 6] = 1
if sum(ct[:3]) == 3 or sum(ct[3:6]) == 3 or sum(ct[6:9]) == 3:
    print('Yes')
elif ct[0] + ct[4] + ct[8] == 3 or ct[2] + ct[4] + ct[6] == 3:
    print('Yes')
elif ct[0] + ct[3] + ct[6] == 3 or ct[1] + ct[4] + ct[7] == 3 or ct[2] + ct[5] + ct[8] == 3:
    print('Yes')
else:
    print('No')
