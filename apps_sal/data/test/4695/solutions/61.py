x, y = map(int, input().split())
s1 = {1, 3, 5, 7, 8, 10, 12}
s2 = {4, 6, 9, 11}
print(["No", "Yes"][(x in s1 and y in s1) or (x in s2 and y in s2)])
