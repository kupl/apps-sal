q = int(input())
for _ in range(q):
    l, r, d = list(map(int, input().split()))
    if d >= l:
        p = r // d + 1
        print(p * d)
    else:
        print(d)
