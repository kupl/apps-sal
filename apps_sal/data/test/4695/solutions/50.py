x, y = map(int, input().split())
group_A = [1, 3, 5, 7, 8, 10, 12]
group_B = [4, 6, 9, 11]
if x in group_A and y in group_A:
    print("Yes")
elif x in group_B and y in group_B:
    print("Yes")
else:
    print("No")
