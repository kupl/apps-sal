t = 1
for test in range(t):
    n = int(input())
    a = input()
    b = input()
    count = 0
    for i in range(n // 2):
        arr = [a[i], a[n - i - 1], b[i], b[n - i - 1]]
        tmp = len(set(arr))
        if tmp == 4:
            count += 2
        elif tmp == 1:
            continue
        elif tmp == 2:
            arr.sort()
            if arr[0] == arr[2] or arr[1] == arr[3]:
                count += 1
        elif a[i] == a[n - i - 1]:
            count += 2
        else:
            count += 1
    if n % 2 == 1 and a[n // 2] != b[n // 2]:
        count += 1
    print(count)
