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
            ext = max(ext, 2)
        else:
            ext = max(ext, 1)
    ans += ext
    print(ans)


__starting_point()
