n = int(input())
d = {}
for i in range(n - 1):
    (a, b) = list(map(int, input().split()))
    try:
        d[a].append(b)
    except:
        d[a] = [b]
    try:
        d[b].append(a)
    except:
        d[b] = [a]
array = list(map(int, input().split()))
flag = 0
if array[0] == 1:
    i = 1
    j = 0
    while j < n and i < n:
        if array[j] in d[array[i]]:
            i += 1
        else:
            j += 1
    if j == n and i != n:
        flag = 1
else:
    flag = 1
if flag == 1:
    print('No')
else:
    print('Yes')
