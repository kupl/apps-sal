def __starting_point():
    arr = input().split()
    s = int(arr[0])
    num = int(arr[1])
    count = 0
    for i in range(1, s + 1):
        if i > num + 1:
            break
        if num % i == 0 and num / i <= s:
            count += 1
    print(count)


__starting_point()
