n = int(input())
for i in range(n):
    s = input()
    se = set()
    a = []
    for j in s:
        se.add(j)
        a.append(j)
    if len(se) == 1:
        print(-1)
    else:
        a.sort()
        for j in a:
            print(j, end='')
        print()
