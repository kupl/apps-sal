num = int(input())

range_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for _ in range_num:
    if num / _ in range_num:
        print("Yes")
        break
else:
    print("No")
