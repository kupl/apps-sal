n = int(input())
L = list(map(int, input().split()))
ans = 'Yes'
pre = -999

for i in range(n):
    if pre <= L[i] - 1:
        pre = L[i] - 1
    elif pre <= L[i]:
        pre = L[i]
    else:
        print('No')
        return
print('Yes')
