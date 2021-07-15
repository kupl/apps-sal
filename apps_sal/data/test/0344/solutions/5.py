t = input()
L = ['a', 'e', 'i', 'o', 'u', 'n']
M = ['a', 'e', 'i', 'o', 'u']
t = t+'n'
b = True
for i in range(len(t)-1):
    if t[i] not in L and t[i+1] not in M:
        b = False
if b:
    print("YES")
else:
    print("NO")

