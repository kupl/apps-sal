input()
p = list(enumerate(map(int, input().split()), 1))
p.sort(key = lambda i: i[1])
print(p[-1][0], p[-2][1])
