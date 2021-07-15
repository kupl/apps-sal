import sys

n = int(input())
a = [int(x) for x in input().split()]
aa = list(set(a))
aa.sort()

if len(aa) > 3:
    print("NO")
    return
if len(aa) < 3:
    print("YES")
    return
if (aa[0] + aa[2]) % 2 != 0:
    print("NO")
    return

if 2 * aa[1] == aa[0] + aa[2]:
    print("YES")
else:
    print("NO")

