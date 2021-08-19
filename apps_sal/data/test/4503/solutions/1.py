(H, N) = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(0, N):
    H -= lst[i]
if H <= 0:
    print('Yes')
else:
    print('No')
