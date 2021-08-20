input()
n = [int(x) for x in input().split()]
n = sorted(set((x for x in n if x > 0)))
print(len(n))
