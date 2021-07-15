N = int(input())
a = sorted([int(x) for x in input().split()])

print(max(a) - min(a))
