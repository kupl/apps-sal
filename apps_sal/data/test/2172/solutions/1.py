n, m = map(int, input().split())
first = dict()
second = dict()
for i in range(m):
    s1, s2 = input().split()
    first[s1] = s2
    second[s2] = s1


lection = input().split()
for i in lection:
    if len(i) > len(first[i]):
        print(first[i], end=' ')
    else:
        print(i, end=' ')
