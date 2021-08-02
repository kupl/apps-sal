q = int(input())
for i in range(q):
    l, r, d = list(map(int, input().split()))
    if d < l:
        print(d)
    else:
        print(r // d * d + d)
