N = int(input())
L = list(map(int, input().split()))
a = max(L)
L.remove(a)
s = 0
for i in L:
    s += i

if a < s:
    print('Yes')
else:
    print('No')
