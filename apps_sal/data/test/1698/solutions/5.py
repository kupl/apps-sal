n, k = [int(x) for x in input().split()]
f = [int(x) - 1 for x in input().split()]
f.sort()
assert len(f) == n
print(2 * sum(f[-1::-k]))
