n = int(input())
A = list(map(int, input().split()))
summa = 0
d = dict()
ans = set()
for i in range(len(A)):
    elem = A[i]
    summa += elem
    try:
        d[elem].add(i)
    except:
        d[elem] = set()
        d[elem].add(i)
for i in range(len(A)):
    elem = A[i]
    if summa - elem <= elem:
        continue
    x = summa - elem * 2
    if x in d.keys():
        s = d[x]
        for j in s:
            if j != i:
                ans.add(j)
print(len(ans))
if len(ans) != 0:
    for i in ans:
        print(i + 1, end=' ')
