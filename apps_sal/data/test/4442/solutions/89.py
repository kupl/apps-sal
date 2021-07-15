a, b = list(map(int, input().split()))

lists = [str(a) * b, str(b) * a]
sort_list = sorted(lists)

print((sort_list[0]))

