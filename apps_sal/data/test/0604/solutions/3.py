n = int(input())
a = [int(v) for v in input().split()]
print(len(set(a) - {0}))
