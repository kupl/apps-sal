import collections
N = int(input())
S = []

for i in range(N):
    S.append(input())

c = collections.Counter(S).most_common()
ans = []

if len(c) == 1:
    ans = c
else:
    for k in range(N):
        if c[0][1] == c[k][1]:
            ans.append(c[k])
        else:
            break
for x in sorted(ans):
    print(x[0])
