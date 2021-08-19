n = int(input())
l = list(map(int, input().split()))
print(max(abs(1 - (l.index(n) + 1)), abs(n - (l.index(n) + 1)), abs(n - (l.index(1) + 1)), abs(1 - (l.index(1) + 1))))
