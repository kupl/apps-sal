n = int(input())
ar = list(map(int, input().split()))

mn = min(ar)
mx = max(ar)
if mx - mn < 2:
    print(n)
    print(' '.join([str(i) for i in ar]))
    return
a=0
b=0
c =0
for i in ar:
    if i == mn:
        a +=1
    elif i == mx:
        c +=1
    else:
        b+=1
cans1 = b - (b%2)
cans2 = 2*min(a,c)
if cans1 > cans2:
    ans = []
    for i in range(a):
        ans.append(mn)
    for i in range(c):
        ans.append(mx)
    for i in range(b//2):
        ans.append(mn)
        ans.append(mx)
    if len(ans) < n:
        ans.append(mn+1)
    print(n-cans1)
    print(' '.join([str(i) for i in ans]))
else:
    ans = []
    if c > a:
        ans = [mx for i in range(c-a)]
        while len(ans) < n:
            ans.append(mn+1)
    else:
        ans = [mn for i in range(a-c)]
        while len(ans) < n:
            ans.append(mn+1)
    print(n-cans2)
    print(' '.join([str(i) for i in ans]))
