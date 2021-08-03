q = int(input())
for _ in range(q):
    r, c = list(map(int, input().split()))
    print("W" + (c - 1) * "B")
    for i in range(r - 1):
        print("B" * c)
