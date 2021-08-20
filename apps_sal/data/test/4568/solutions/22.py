n = int(input())
s = input()
L = ''
R = ''
C = ''
tmp = 0
ans = []
for i in range(1, len(s)):
    L = s[:i]
    R = s[i:]
    C = len(set(L) & set(R))
    ans.append(C)
    L = ''
    R = ''
print(max(ans))
