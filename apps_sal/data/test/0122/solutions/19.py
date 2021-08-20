def func():
    n = int(input())
    array = []
    sum = 0
    for (index, number) in enumerate(input().split()):
        num = int(number)
        array.append(num)
        sum += num
    if sum % 1 == 1:
        print('NO')
        return
    setn = set()
    sumSub = 0
    indexdict = {}
    for (indexm, number) in enumerate(array):
        sumSub += number
        sum2 = sumSub * 2 - sum
        if sum2 % 2 == 1:
            continue
        sum2 /= 2
        setn.add(sum2)
        indexdict[sum2] = indexm
    i = 0
    if 0 in setn:
        print('YES')
        return
    while i < n:
        num = array[i]
        if num in setn and num in indexdict and (i < indexdict[num]):
            print('YES')
            return
        if -num in setn and -num in indexdict and (i > indexdict[-num]):
            print('YES')
            return
        i += 1
    print('NO')


func()
