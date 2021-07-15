tests = int(input())
for t in range(tests):
    n = int(input())
    ls = list(map(int, input().split()))
    curr = 0
    res = 0
    for item in ls:
        curr += item
        if curr < res:
            res = curr
    print(-res)
