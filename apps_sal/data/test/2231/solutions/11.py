import sys
t = int(sys.stdin.readline())
arrz = []
for l in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    flag = 0
    arr2 = []
    dict1 = {}
    for i in range(n):
        try:
            dict1[arr[i]] += 1
            if(dict1[arr[i]] == 2):
                arr2.append(arr[i])
                dict1[arr[i]] = 0
        except:
            KeyError
            dict1[arr[i]] = 1

    fans = arr2[1] / arr2[0]
    index = 0
    for i in range(len(arr2) - 1):
        if(arr2[i + 1] / arr2[i] < fans):
            fans = arr2[i + 1] / arr2[i]
            index = i
    arrz.append('%d %d %d %d' % (arr2[index], arr2[index], arr2[index + 1], arr2[index + 1]))
print('\n'.join(arrz))
