n = int(input())
a = [int(v) for v in input().split()]
MAX = 10**6 + 1
L = [0] * MAX
for v in a:
    L[v] = 1
    
for i in range(n):
    if L[a[i]]:
        for x in range(a[i] * 2, MAX, a[i]):
            if L[x]:
                L[x] = max(L[x], L[a[i]] + 1)
print(max(L))
