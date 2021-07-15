A, B, C = map(int, input().split())
lst = [A, B, C]
lst2 = sorted(lst, reverse=True)
lst3 = list(map(str, lst2))
print(int(lst3[0] + lst3[1]) + int(lst3[2]))
