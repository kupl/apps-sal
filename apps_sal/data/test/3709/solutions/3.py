(n, k) = list(map(int, input().split()))
probs = list(([0] * n for _ in range(k)))
pbtype = [0] * 2 ** k
e = [False] * 2 ** k
ei = [False] * k
for i in range(n):
    x = list(map(int, input().split()))
    sum = 0
    for j in range(k):
        if x[j] == 0:
            sum += 2 ** j
            ei[j] = True
    pbtype[sum] += 1
    e[sum] = True
success = False
if e[2 ** k - 1]:
    success = True
for i in range(k):
    if e[2 ** k - 1 - 2 ** i] and ei[i]:
        success = True
if k == 4:
    if e[3] and e[12]:
        success = True
    if e[6] and e[9]:
        success = True
    if e[5] and e[10]:
        success = True
if success:
    print('YES')
else:
    print('NO')
