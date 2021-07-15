group1 = [1, 3, 5, 7, 8, 10, 12]
group2 = [4, 6, 9, 11]

x, y = map(int, input().split())

if (x in group1 and y in group1) or (x in group2 and y in group2) or (x == y == 2):
    print("Yes")
else:
    print("No")
