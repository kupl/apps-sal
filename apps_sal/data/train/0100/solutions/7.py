q = int(input())
for i in range(q):
    r = [int(x) for x in input().split()]
    print(min(int(sum(r) / 2), sum(r) - max(r)))
