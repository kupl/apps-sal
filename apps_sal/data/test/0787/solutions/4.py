n = int(input())
s = input()
t = []
k = []
for i in range(len(s)):
    if s[i] not in t:
        t.append(s[i])
        k.append(i)
if len(t) < n:
    print("NO")
else:
    print("YES")
    for u in range(n - 1):
        print(s[k[0]:k[1]])
        k.pop(0)
    print(s[k[0]:])
