s = input()
a, b = list(map(int, input().split()))
n = len(s)
flag = 0
p = 0
pfx = []
for i, c in enumerate(s, 1):
    p = (p * 10 + int(c)) % a

    if(i < n and p == 0 and s[i] != '0'):
        pfx.append(i)
q = 0
p = 1
i = len(s)
for j in reversed(pfx):
    for i in range(i - 1, j - 1, -1):
        q = (q + int(s[i]) * p) % b
        p = p * 10 % b
    if not q:
        print("YES")
        print(s[:i])
        print(s[i:])
        return
print("NO")
