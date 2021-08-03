def decSeq(L):
    l, r = 0, 0
    for i in range(len(L) - 1):
        if L[i + 1] < L[i]:
            l = i
            break
    try:
        for i in range(l, len(L)):
            r = i
            if L[i + 1] > L[i]:
                break
    except IndexError:
        r = len(L) - 1
    return l, r


n, arr = input(), list(map(int, input().split()))

l, r = decSeq(arr)

if sorted(arr) == arr:
    print('yes')
    print(1, 1)
elif sorted(arr) == arr[:l] + sorted(arr[l:r + 1]) + arr[r + 1:]:
    print('yes')
    print(l + 1, r + 1)
else:
    print('no')
