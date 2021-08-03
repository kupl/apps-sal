N = int(input())
a = [int(v) for v in input().split(" ")]

max_v = max(a)
min_v = min(a)

print((max_v - min_v))
