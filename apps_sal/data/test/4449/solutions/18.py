q = int(input())
for Q in range(q):
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = []
    unused = set()
    for i in arr:
        if i not in unused:
            unused.add(i)
        else:
            arr2.append(i)
            unused.remove(i)
    if len(unused) != 0:
        print('NO')
    else:
        flag = True
        arr2.sort()
        s = arr2[0] * arr2[-1]
        arr2 = arr2[1:-1]
        while len(arr2) != 0:
            s2 = arr2[0] * arr2[-1]
            if s2 != s:
                print('NO')
                flag = False
                break
            else:
                arr2 = arr2[1:-1]
        if flag:
            print('YES')
