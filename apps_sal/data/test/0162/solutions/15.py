n, k = [int(v) for v in input().split()]
aa = [int(v) for v in input().split()]

print(min(k // a for a in aa if k % a == 0))

