import collections
N = int(input())
A = list(map(int, input().split()))
ans = 1
if 0 in A:
    A.remove(0)
Acounter = collections.Counter(A)
for i in Acounter.values():
    if i == 2:
        continue
    else:
        ans = 0
        break
if ans == 0:
    pass
if ans != 0:
    for i in range(N // 2):
        ans = ans * 2 % (10 ** 9 + 7)
print(ans)
