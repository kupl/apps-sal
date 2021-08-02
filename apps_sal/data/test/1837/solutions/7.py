def __starting_point():
    inp = input()
    inp = input()
    arr = inp.split()
    ans = 0
    ext = 0
    for i in range(len(arr)):
        if i == int(arr[i]):
            ans += 1

        elif int(arr[int(arr[i])]) == i:
            # print("Matches")
            # print(i,end=':')
            # print(arr[int(arr[i])])
            ext = max(ext, 2)
        else:
            # print(i,end=':')
            # print(arr[int(arr[i])])
            ext = max(ext, 1)
# print(ans)
    ans += ext
    print(ans)


__starting_point()
