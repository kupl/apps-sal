(n, m) = [int(val) for val in input().split()]
s = input()
t = input()
ans = 100000000
ansL = []
for i in range(m - n + 1):
    val = 0
    valL = []
    for j in range(n):
        if s[j] != t[j + i]:
            val += 1
            valL.append(j + 1)
    if val < ans:
        ans = val
        ansL = valL
print(ans)
for ind in ansL:
    print(ind, end=' ')
