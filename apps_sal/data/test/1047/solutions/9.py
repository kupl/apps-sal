n = int(input())
k = n
ans = []
while k != 0:
    s = str(k)
    bin = ''
    for c in s:
        if c == '0':
            bin += '0'
        else:
            bin += '1'
    d = int(bin)
    ans.append(d)
    k -= d
print(len(ans))
print(' '.join(map(str, ans)))
