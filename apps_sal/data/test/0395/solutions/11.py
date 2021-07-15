import itertools
A = list(map(int, input().split()))
B = itertools.permutations(A)
ans = False
for i in B:
    if sum(i[:3]) == sum(i[3:]):
        ans = True
        break
if ans:
    print("YES")
else:
    print("NO")
