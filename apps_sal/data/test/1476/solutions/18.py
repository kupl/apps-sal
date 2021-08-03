num = int(input())

if num == 3:
    print("2")
    print("1 3")
elif num == 2 or num == 1:
    print("1")
    print("1")
elif num == 4:
    print("4")
    print("3 1 4 2")
else:
    all = [x for x in range(1, num + 1, 2)] + [x for x in range(2, num + 1, 2)]
    print(len(all))
    print(str(all).replace("[", "").replace(",", "").replace("]", ""))
