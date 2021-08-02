q = int(input())
for fwewfe in range(q):
    n = int(input())
    sk = 1
    su = 0
    while su < n:
        su += sk
        sk *= 3
    while su >= n and sk > 0:
        if su - sk >= n:
            su -= sk
        sk //= 3
    print(su)
