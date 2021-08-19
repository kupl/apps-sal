def test():
    arr = []
    ans = 0
    first_input = input()
    first_num = first_input.split()
    a = int(first_num[0])
    b = int(first_num[1])
    sec_input = input()
    sec_num = sec_input.split()
    if len(sec_num) == a:
        pass
    else:
        print('Wrong input')
    for i in sec_num:
        arr.append(int(i))
    for i in range(0, len(arr) - 1):
        num = arr[i]
        num_2 = arr[i + 1]
        if num_2 - num > b:
            ans += b
        else:
            ans += num_2 - num
    ans += b
    print(ans)


test()
