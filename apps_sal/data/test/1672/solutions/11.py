while(1):
    try:
        n = int(input())
        a = []
        for i in range(0, n):
            b = input()
            a.append(b)
        count = 1
        for i in range(1, n - 1):
            if a[i] == a[i - 1]:
                continue
            if a[i + 1] == a[i - 1] and a[i - 1] != a[i]:
                count += 1
            else:
                count += 1
        if a[n - 1] != a[n - 2]:
            count += 1
        print(count)
    except EOFError:
        break
