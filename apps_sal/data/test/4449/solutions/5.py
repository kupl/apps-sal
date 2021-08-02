for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    i = 1
    j = len(a) - 2
    ans = "YES"
    area = a[0] * a[-1]
    while i < j:
        if a[i] == a[i - 1] and a[j] == a[j + 1] and a[i] * a[j] == area:
            i += 2
            j -= 2
        else:
            ans = "NO"
            break
    print(ans)
