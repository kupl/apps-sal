
n = int(input())
participants = {}
order = True
while n:
    n -= 1
    x, k = list(map(int, input().split()))
    if k in participants:
        if x in participants[k]:
            continue
        elif x - 1 in participants[k]:
            participants[k].add(x)
        else:
            order = False
            break
    else:
        if x != 0:
            order = False
            break
        tmp = set()
        tmp.add(x)
        participants[k] = tmp


if order:
    print("YES")
else:
    print("NO")
