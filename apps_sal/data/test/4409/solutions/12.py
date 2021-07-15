from collections import defaultdict as ddict

n = int(input())
a = list(map(int, input().split()))
count = ddict(list)
main_key = 0
max_len = 0

for i, it in enumerate(a):
    count[it].append(i)
for k in count:
    if len(count[k]) > max_len:
        max_len = len(count[k])
        main_key = count[k][0]
if max_len == n:
    print(0)
    return

ans = list()
for i in range(main_key-1, -1, -1):
    if a[i] == a[main_key]: continue
    if a[i] > a[main_key]: ans.append((2, i+1, i+2))
    else: ans.append((1, i+1, i+2))

for i in range(main_key+1, n):
    if a[i] == a[main_key]: continue
    if a[i] > a[main_key]: ans.append((2, i+1, i))
    else: ans.append((1, i+1, i))

print(len(ans))
for it in ans:
    print('%d %d %d'%(it))

