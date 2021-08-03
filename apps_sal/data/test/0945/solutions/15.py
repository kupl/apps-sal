def test():
    n = int(input())
    points = list(map(int, input().split()))
    for i in range(n - 1):
        a = points[i]
        b = points[i + 1]
        if(a > b):
            temp = a
            a = b
            b = temp
        for j in range(i):
            if(points[j] >= a and points[j] <= b):
                if(j > 0 and (points[j - 1] < a or points[j - 1] > b or points[j + 1] < a or points[j + 1] > b)):
                    print('yes')
                    return 0
                elif(j == 0 and (points[j + 1] < a or points[j + 1] > b)):
                    print('yes')
                    return 0

    return 1


if(test()):
    print('no')
