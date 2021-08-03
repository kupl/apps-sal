t = int(input())
for i in range(t):
    a = [int(x) for x in list(input())]
    n = len(a)
    zero = 0
    arr = 0
    for i in range(n):
        if a[i] == 1:
            size = 2
            num = 1
            arr += 1
            if i != n - 1:
                j = i + 1
                if a[j] == 1:
                    num *= 2 + 1
                else:
                    num *= 2

                while num <= size + zero and num >= size:
                    arr += 1
                    if j == n - 1:
                        break
                    j += 1
                    if a[j] == 1:
                        num = num * 2 + 1
                    else:
                        num *= 2
                    size += 1
            zero = 0
        else:
            zero += 1
    print(arr)
