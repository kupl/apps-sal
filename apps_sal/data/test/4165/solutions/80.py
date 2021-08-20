N = int(input())
L = sorted(list(map(int, input().split())))
m = L[-1]
s = sum(L[:-1])
if m < s:
    print('Yes')
else:
    print('No')
