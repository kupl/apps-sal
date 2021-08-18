
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
mp = defaultdict(list)
addition = sum(a)
ans = []
for i in range(n):
    mp[a[i]].append(i)
index = 0
# print(mp)
for i in a:
    temp = addition
    temp -= i
    # print("add ",temp )
    if temp % 2 == 1:
        index += 1
        continue
    temp //= 2
    # print("now temp ",temp)

    if temp in mp and len(mp[temp]) > 1:

        ans.append(index + 1)

    if i in mp and len(mp[temp]) == 1:
        # print("here")
        if mp[temp][0] != index:
            ans.append(index + 1)
            # print("appended")
    index += 1
print(len(ans))
if len(ans) == 0:
    return
ans = list(map(str, ans))
print(' '.join(ans))
