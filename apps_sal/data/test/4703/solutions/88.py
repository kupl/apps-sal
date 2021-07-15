from itertools import product
s = input()
n = len(s)
ans = 0
for lst in product(['x', ' '], repeat=n-1):
    ss = ''
    for i in range(n-1):
        ss += (s[i] + str(lst[i]))
    ss += s[-1]
    ss = ss.replace('x', '')
    temp = [int(x) for x in ss.split()]
    ans += sum(temp)
print(ans)
