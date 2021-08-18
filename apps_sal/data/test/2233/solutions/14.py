def mi():
    return list(map(int, input().split()))


'''
4
5
souse
houhe
3
cat
dog
2
aa
az
3
abc
bca
'''
for _ in range(int(input())):
    n = int(input())
    a = list(input())
    b = list(input())
    ndiff = 0
    aa, bb = [0] * 2, [0] * 2

    for i in range(n):
        if a[i] != b[i]:
            ndiff += 1
            if ndiff == 3:
                break
            aa[ndiff - 1] = a[i]
            bb[ndiff - 1] = b[i]
    if ndiff == 1 or ndiff > 2:
        print('No')
    else:
        if ndiff == 2:
            if aa[0] != aa[1] or bb[1] != bb[0]:
                print('No')
                continue
        print('Yes')
