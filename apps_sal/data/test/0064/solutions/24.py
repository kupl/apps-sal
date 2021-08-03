n, k = list(map(int, input().split()))
s = input()
c = dict()
for x in s:
    if not x in c:
        c[x] = 1
    else:
        c[x] += 1

no = False
for x in c:
    if c[x] > k:
        print("NO")
        no = True
        break
if not no:
    print("YES")
