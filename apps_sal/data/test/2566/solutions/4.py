def solve():
    k = int(input())
    w = tuple(map(int, input().split()))
    
    cnt = sum(w)
    weeks, k = divmod(k - 1, cnt)

    d = 1 << 32
    for i in range(7):
        c = 0
        for j in range(7):
            c += w[(i + j) % 7]
            if c == k + 1:
                d = min(d, j + 1)
                break
    
    print(7 * weeks + d)

for _ in range(int(input())):
    solve()

