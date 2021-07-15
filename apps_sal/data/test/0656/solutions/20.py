n, k = list(map(int,input().split()))
a = list([int(x)>=0 for x in input().split()])

for ind_positive in range(n):
    if not a[ind_positive]:
        break
else:
    print(0)
    return
a = a[ind_positive:]
n = len(a)

for ind_positive in range(n-1, -1, -1):
    if not a[ind_positive]:
        break
a = a[:ind_positive+1]
len_suf = n-ind_positive-1
n = len(a)
#print(a, len_suf)

b = []
i = 0
while True:
    j = 0
    while i < n and a[i]:
        i += 1
        j += 1
    if j:
        b.append(j)
    i += 1
    if i >= n:
        break
b_sort = b.copy()
b_sort.sort(reverse = True)
s = 0
i = 0
if n-s>k:
    for i in range(len(b)):
        s += b_sort[i]
        if n-s <= k:
            i += 1
            break
if n-s > k:
    ans2 = -1
else:
    ans2 = i*2+2

k -= len_suf
if k < 0:
    ans1 = -1
else:
    b = []
    i = 0
    while True:
        j = 0
        while i < n and a[i]:
            i += 1
            j += 1
        if j:
            b.append(j)
        i += 1
        if i >= n:
            break
    b_sort = b.copy()
    b_sort.sort(reverse = True)
    s = 0
    i = 0
    if n-s>k:
        for i in range(len(b)):
            s += b_sort[i]
            if n-s <= k:
                i += 1
                break
    if n-s > k:
        ans1 = -1
    else:
        ans1 = i*2+1

if ans1 == -1:
    print(ans2)
elif ans2 == -1:
    print(ans1)
else:
    print(min(ans1,ans2))









