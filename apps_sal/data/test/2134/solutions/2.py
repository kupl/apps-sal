def bitcode(lis):
    bc = []
    for n in lis:
        if lis[n] > 1:
            bc.append(n)
    return bc


n = int(input())
lis = {}
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for bc in a:
    try:
        lis[bc] += 1
    except:
        lis[bc] = 1

bcs = bitcode(lis)
if len(bcs) == 0:
    print(0)
else:
    bsum = 0
    for i in range(n):
        if lis[a[i]] > 1:
            bsum += b[i]
            continue
        for bc in bcs:
            if (a[i] & ~bc) == 0:
                bsum += b[i]
                break
    print(bsum)
