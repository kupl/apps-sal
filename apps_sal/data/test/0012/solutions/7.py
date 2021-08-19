n = int(input())
s = input()
golden_sub = s.split('S')
nG = 0
for c in s:
    if c == 'G':
        nG += 1
t = len(golden_sub)
if t == 1:
    print(len(golden_sub[0]))
else:
    ans = 0
    for i in range(t - 1):
        l1 = len(golden_sub[i])
        l2 = len(golden_sub[i + 1])
        if l1 + l2 < nG:
            ans = max(ans, l1 + l2 + 1)
        else:
            ans = max(ans, l1 + l2)
    print(ans)
