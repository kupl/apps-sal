n = (int(input()))
j = list(map(int, input().split()))
b = 0
e = 0
ans = []
subline = set()
while e < n:
    perl = j[e]
    if perl in subline:
        ans += [[b + 1, e + 1]]
        subline = set()
        b = e + 1
        e += 1
    else:
        subline.add(perl)
        e += 1
if len(ans) == 0:
    print(-1)
else:

    ans[-1][1] = n
    print(len(ans))

    for i in range(len(ans)):
        print(' '.join(list(map(str, ans[i]))))
