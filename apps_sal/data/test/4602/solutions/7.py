N = int(input())
K = int(input())
print((sum([min(int(a), K - int(a)) for a in input().split()]) * 2))

