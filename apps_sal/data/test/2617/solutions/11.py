T = int(input())
for case in range(T):
    n = int(input())
    # print("target",n)
    o = 0
    arr = []
    while 2 ** o - 1 < n:
        arr.append(2 ** o)
        o += 1
    diff = 2 ** o - 1 - n
    # print(arr)
    # print("min",o,"diff",diff)
    b = str(bin(diff))[2:][::-1]
    # print(b)
    o2 = 0
    arr2 = []
    while o2 < len(b):
        if b[o2] == "0":
            pass
            # arr2.append(0)
        else:
            arr2.append(2 ** o2)
        o2 += 1
    # print(arr,arr2)
    delta = len(arr) - len(arr2)
    for i in range(delta, len(arr2) + delta):
        arr[i] -= arr2[i - delta]
    # print(arr)
    ret = []
    for i in range(len(arr) - 1):
        ret.append(str(arr[i + 1] - arr[i]))
    days = len(ret)
    ret = " ".join(ret)
    print(days)
    print(ret)
