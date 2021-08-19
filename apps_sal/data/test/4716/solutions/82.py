k = list(map(int, input().split()))[1]
ls = list(sorted(list(map(int, input().split()))))
print(sum(ls[len(ls) - k:]))
