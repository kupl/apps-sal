a = map(int, input().split())
paint_list = list(a)

if paint_list[0] == paint_list[1] == paint_list[2]:
    print(1)
elif paint_list[0] == paint_list[1] and paint_list[0] != paint_list[2]:
    print(2)
elif paint_list[0] == paint_list[2] and paint_list[0] != paint_list[1]:
    print(2)
elif paint_list[1] == paint_list[2] and paint_list[0] != paint_list[1]:
    print(2)
else:
    print(3)
