from math import ceil, log
t = 1
for test in range(t):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = []
    for key in a:
        if key in b:
            ans.append(key)
    print(*ans)
