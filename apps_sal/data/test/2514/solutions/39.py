import collections
n = int(input())
a = list(map(int,input().split()))
q = int(input())
bc = [[int(i) for i in input().split()] for _ in range(q)]

total = sum(a)
s = collections.Counter(a)


for x in range(q):
    if bc[x][0] in s and bc[x][1] in s:
        s[bc[x][1]] += s[bc[x][0]]
        total += (bc[x][1]-bc[x][0]) * s[bc[x][0]]
        del s[bc[x][0]]
    elif bc[x][0] in s and bc[x][1] not in s:
        s[bc[x][1]] = s[bc[x][0]]
        total += (bc[x][1]-bc[x][0]) * s[bc[x][0]]
        del s[bc[x][0]]
    print(total)
