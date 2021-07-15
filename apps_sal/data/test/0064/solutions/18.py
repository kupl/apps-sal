n, k = [int(i) for i in input().split()]
s = input()
m = [0] * 1000
for c in s:
    m[ord(c)] += 1
if max(m) > k:
    print("NO")
else:
    print("YES")

