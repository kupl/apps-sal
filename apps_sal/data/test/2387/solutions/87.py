def CNT(A):
    tmp, Min = 0, 0
    for a in A:
        if a == '(': tmp += 1
        else: tmp -= 1
        Min = min(Min, tmp)
    return (-Min, tmp-Min)

N = int(input())
S = [input() for _ in range(N)]
T = [CNT(s) for s in S]

pls = []
mis = []
for l, r in T:
    if l <= r: pls.append((l, r))
    else: mis.append((l, r))

pls.sort(key=lambda a: a[0])
mis.sort(key=lambda a: a[1], reverse=True)
totl= pls + mis

levl = 0
for l, r in totl:
    levl -= l
    if levl < 0:
        print('No')
        return
    levl += r

print('Yes' if levl==0 else 'No')
