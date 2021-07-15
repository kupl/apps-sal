d = sorted(map(int, input().split()))
print(min(sum(d), 2 * sum(d[:2])))
