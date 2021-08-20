(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
cs = dict()
ans = []
for num in a:
    if num in cs:
        cs[num] += 1
    else:
        cs[num] = 1
    if len(cs) == n:
        new = dict()
        for i in list(cs.keys()):
            if cs[i] > 1:
                new[i] = cs[i] - 1
        cs = new
        ans.append('1')
    else:
        ans.append('0')
print(''.join(ans))
