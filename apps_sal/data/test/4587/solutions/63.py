import bisect
n = int(input())
X = sorted(list(map(int, input().split())))
Y = sorted(list(map(int, input().split())))
Z = sorted(list(map(int, input().split())))
print(sum(bisect.bisect_left(X, b) * (n - bisect.bisect_right(Z, b)) for b in Y))
