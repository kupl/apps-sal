(n1, n2) = list(map(int, input().split()))
n = list(map(int, input().split()))
k = sorted(list(map(int, input().split())))[::-1]
t = 0
for i in range(n1):
    if n[i] == 0:
        n[i] = k[t]
        t += 1
if sorted(n) == n:
    print('No')
else:
    print('Yes')
