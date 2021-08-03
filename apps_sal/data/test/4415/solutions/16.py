from collections import Counter
n = int(input())
l = list(map(int, input().split()))

d = Counter(l)

if max(d.values()) > 2:
    print("NO")
else:
    inc = []
    dec = []

    for i in d:
        if d[i] == 2:
            inc.append(i)
            dec.append(i)
        else:
            inc.append(i)

    n1 = len(inc)
    n2 = len(dec)
    print("YES")
    if n1:
        print(n1)
        inc.sort()
        print(*inc)
    else:
        print(n1)
        print()

    if n2:
        print(n2)
        dec.sort(reverse=True)
        print(*dec)
    else:
        print(n2)
        print()
