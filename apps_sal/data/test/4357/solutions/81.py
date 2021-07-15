l = list(map(int, input().split()))
i = l.index(max(l))
print(l.pop(i) * 10 + sum(l))
