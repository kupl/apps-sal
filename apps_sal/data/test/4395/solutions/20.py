n = int(input())
s = input()
c = ['RGB', 'RBG', 'GRB', 'GBR', 'BRG', 'BGR']
ans = 10**9
ss = ''
for base in c:
    x = base * (len(s) // 3 + 1)
    t = 0
    for j in range(len(s)):
        if s[j] != x[j]: t += 1
    if t < ans:
        ans = t
        ss = x[:len(s)]
print(ans)
print(ss)
