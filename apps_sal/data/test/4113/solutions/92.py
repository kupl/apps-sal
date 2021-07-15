n = int(input())

if n >= 18:
    print("Yes")
    return

ans_list = [4,7,8,11,12,14,15,16]

if n in ans_list:
    print("Yes")
    return

else:
    print("No")
