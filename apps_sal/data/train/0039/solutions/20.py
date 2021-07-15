t = int(input())
for _ in range(t):
    a,b,p = map(int,input().split())
    sl = list(input())
    before = ""
    for idx, i in enumerate(sl[::-1][1:]):
        cost = a if i == "A" else b
        if before == i:
            continue
        if cost > p:
            break
        else:
            before = i
            p -= cost
    else:
        print(1)
        continue
    print(len(sl) - idx)
