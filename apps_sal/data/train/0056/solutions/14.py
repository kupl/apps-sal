import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    res = [["0"] * n for _ in range(n)]
    if k % n:
        print(2)
    else:
        print(0)
    for d in range(n):
        for i in range(n):
            if k == 0:
                break
            res[i][(i + d) % n] = "1"
            k -= 1
    for r in res:
        print("".join(r))
