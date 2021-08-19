(n, m, x) = map(int, input().split())
am = sorted(map(int, input().split()))
print(min(len(list(filter(lambda a: a < x, am))), len(list(filter(lambda a: x < a, am)))))
