(n, q) = map(int, input().split())
l = list(map(int, input().split()))
mini = min(l)
maxi = max(l)
for i in range(q):
    m = int(input())
    if m <= maxi and m >= mini:
        print('Yes')
    else:
        print('No')
