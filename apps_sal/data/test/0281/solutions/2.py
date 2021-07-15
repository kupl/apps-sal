def __starting_point():
    arr = input().split(' ')
    ans = 1
    a = int(arr[0])
    b = int(arr[1])
    while ans!=0 and b>a:
        ans = (b%10)*ans
        ans = ans%10
        b -= 1
    print(ans)

__starting_point()
