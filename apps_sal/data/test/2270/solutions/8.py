from collections import Counter
n = int(input())
a = list(map(int, input().split()))
q = int(input())
c = Counter(a)
d = {2: {}, 4: {}}
for i in c:
    if c[i] >= 4:
        d[4][i] = 0
    elif c[i] >= 2:
        d[2][i] = 0


for i in range(q):
    a, b = input().split()
    b = int(b)
    if a == "+":
        if b in c:
            c[b] += 1
        else:
            c[b] = 1
        if c[b] == 4:
            d[4][b] = 0
            del d[2][b]
        elif c[b] == 2:
            d[2][b] = 0
    else:
        c[b] -= 1
        if c[b] == 3:
            del d[4][b]
            d[2][b] = 0
        elif c[b] == 1:
            del d[2][b]

    if len(d[4]) >= 2:
        print("YES")
    elif len(d[4]) == 1 and len(d[2]) >= 2:
        print("YES")
    elif len(d[4]) == 1:
        for k in d[4]:
            ind = k
            break
        if len(d[2]) == 1 and c[ind] >= 6:
            print("YES")
        elif len(d[2]) == 0 and c[ind] >= 8:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
