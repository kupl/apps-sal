s = input()
k = int(input())
n = len(s)
r = []
for right in range(0, n):
    for left in range(right + 1, right + k + 1):
        r.append(s[right:left])
print(sorted(set(r))[k - 1])
