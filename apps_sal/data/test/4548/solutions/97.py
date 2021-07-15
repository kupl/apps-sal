n, m, x = map(int, input().split())
a_l = list(map(int, input().split()))

for i, a in enumerate(a_l):
    if x < a:
        break
if i > len(a_l)/2:
    ans = len(a_l[i:])
else:
    ans = len(a_l[:i])
print(ans)
