N = int(input())
X = list(map(int, input().split()))

P = int(sum(X)/N+.5)
print(sum((x-P)**2 for x in X))
