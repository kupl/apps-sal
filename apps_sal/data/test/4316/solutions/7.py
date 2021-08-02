S = list(input())
s = set(S)
lis = {}
for x in S:
    if x in lis:
        lis[x] += 1
    else:
        lis[x] = 1
ans = True
if len(lis) == 2:
    for x in s:
        if lis[x] != 2:
            ans = False
else:
    ans = False
if ans:
    print("Yes")
else:
    print("No")
