k, x = map(int, input().split())

lists = []
for i in range(x - k + 1, x + k):
    lists.append(str(i))

print(" ".join(lists))
