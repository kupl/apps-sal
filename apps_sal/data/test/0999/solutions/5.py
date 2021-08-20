l1 = [[int(x.strip().rstrip()) for x in input().split()] for _ in range(int(input()))]
l2 = [[int(x.strip().rstrip()) for x in input().split()] for _ in range(int(input()))]
r1 = max(0, max((x[0] for x in l2)) - min([x[1] for x in l1]))
r2 = max(0, max((x[0] for x in l1)) - min([x[1] for x in l2]))
print(max(r1, r2))
