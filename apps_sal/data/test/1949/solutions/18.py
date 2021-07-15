def __starting_point():
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    count = 0
    for i in range(k):
        if n == 0:
            print(0)
        else:
            rem = arr[-1]
            print(arr[-1]-count)
            count += (arr[-1]-count)
            check = arr[-1]

            while n > 0 and check == arr[-1]:
                arr.pop()
                n -= 1
            '''if n > 0:
                arr[-1] -= check'''

__starting_point()
