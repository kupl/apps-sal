def __starting_point():

    n = int(input())

    res = n

    res -= n//2
    res -= n//3
    res -= n//5
    res -= n//7

    res += n//6
    res += n//10
    res += n//14
    res += n//15
    res += n//21
    res += n//35

    res -= n//(3*5*7)
    res -= n//(2*5*7)
    res -= n//(2*3*7)
    res -= n//(2*3*5)

    res += n//(2*3*5*7)

    print(res)
__starting_point()
