N = int(input())

arr = [[] for _ in range(N)]
for i in range(N):
    A = int(input())
    for a in range(A):
        x, y = map(int, input().split())
        arr[i].append((x - 1, y))

ans = 0
for bit in range(1, 1 << N):
    honest = set()
    unkind = set()
    h = set()
    for i in range(N):
        if bit & (1 << i):
            h.add(i)
            for x, y in arr[i]:
                if y:
                    honest.add(x)
                else:
                    unkind.add(x)

    # print(h,honest,unkind)
    if 0 == len(honest - h) and h.isdisjoint(unkind) and honest.isdisjoint(unkind):
        # print("   ",h,honest,unkind)
        ans = max(len(h), ans)

print(ans)
