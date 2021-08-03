n = int(input())
d = list(map(int, input().split()))
d.sort()
mins = d[int(n / 2) - 1]
maxs = d[int(n / 2)]
print(maxs - mins)
