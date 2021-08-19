# 18:55
l = int(input())
s = bin(l)[2:]
n = len(s)
m = 0
ans = []
for i in range(n - 1):
    ans.append([i + 1, i + 2, 0])
    ans.append([i + 1, i + 2, 2**(n - 2 - i)])
    m += 2
# print(ans,m)
imp = 2 ** (n - 1)
for i in range(n - 1, 0, -1):
    if s[i] == '1':
        ans.append([1, i + 1, imp])
        m += 1
        imp += 2 ** (n - 1 - i)
print(n, m)
for x in ans:
    print(' '.join(list(map(str, x))))
