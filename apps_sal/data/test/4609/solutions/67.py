import collections
N = int(input())
A = []

for i in range(N):
    A.append(int(input()))

cc = collections.Counter(A)
ans = 0
for nums in list(cc.values()):
    if nums % 2 == 1:
        ans += 1
print(ans)
