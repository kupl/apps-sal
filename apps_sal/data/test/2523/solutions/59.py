s = str(input())
n = len(s)

if n == 1:
    print(1)
    return

maxs = []
for i in range(n-1):
    if s[i] != s[i+1]:
        maxs.append(max(i+1, n-i-1))

if maxs != []:
    print(min(maxs))
else:
    print(n)
