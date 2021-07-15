for __ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ar1 = []
    ar2 = []
    for elem in ar:
        num = 0
        while elem % 2 == 0:
            elem //= 2
            num += 1
        ar1.append(num)
        ar2.append(elem)
    ar3 = []
    for i in range(n):
        ar3.append([ar2[i], ar1[i]])
    ar3.sort()
    i = 1
    j = 1
    num = 1
    ans = sum(ar1)
    while i < n:
        while j < n and ar3[j][0] == ar3[j - 1][0]:
            j += 1
        times = j - i
        prev_val = 0
        for h in range(i - 1, min(j, n)):
            ans -= times * (ar3[h][1] - prev_val)
            times -= 1
            prev_val = ar3[h][1]
        i = j + 1
        j = i
    print(ans)
