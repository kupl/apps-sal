n = int(input())
l = list(map(int,input().split()))

odd = []
even = []
for i in l:
    if i%2:
        odd.append(i)
    else:
        even.append(i)

odd.sort()
even.sort()

lo = len(odd)
le = len(even)

if lo == le or lo == le+1 or lo == le-1:
    print(0)
else:

    if le > lo:
        diff = le - lo - 1
        ans = sum(even[:diff])
    else:
        diff = lo - le - 1
        ans = sum(odd[:diff])

    print(ans)

