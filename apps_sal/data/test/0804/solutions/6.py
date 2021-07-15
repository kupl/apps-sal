from collections import defaultdict

ls = defaultdict(int)

s = input()
k = int(input())

if k > len(s):
    print("impossible")
    return

for c in s:
    ls[c] += 1

dif_ls = 0
for (_,v) in list(ls.items()):
    dif_ls += 1

if dif_ls < k:
    print(k - dif_ls)
else:
    print(0)


