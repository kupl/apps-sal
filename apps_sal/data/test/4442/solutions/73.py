a, b = map(int, input().split())

lists = []
lists.append(str(a) * b)
lists.append(str(b) * a)
lists.sort()

print(lists[0])
