
def __starting_point():
    n = int(input())
    a = list(map(float, input().split()))
    a.sort(reverse=True)
    res = 0
    # a is sorted in desc
    while(a):
        res += sum(a)
        a = a[:len(a) // 4]

    print(int(res))


__starting_point()
