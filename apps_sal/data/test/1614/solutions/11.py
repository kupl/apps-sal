n, h = list(map(int, input().split()))
tab = list(map(int, input().split()))
print(sum([1 if x <= h else 2 for x in tab]))
