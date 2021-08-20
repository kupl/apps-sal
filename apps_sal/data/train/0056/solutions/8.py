import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    if k % n:
        print(2)
    else:
        print(0)
    ans = [[0 for i in range(n)] for j in range(n)]
    if k == 0:
        for i in ans:
            print(*i, sep='')
        continue
    for i in range(n):
        for j in range(n):
            ans[j][(i + j) % n] = 1
            k -= 1
            if k == 0:
                break
        else:
            continue
        break
    for i in ans:
        print(*i, sep='')
