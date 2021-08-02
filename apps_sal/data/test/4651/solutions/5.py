for _ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    k = n - 1
    i = 0
    while i < n:
        mini = l[i]
        ind = -1
        j = i + 1
        while j < min(n, i + k + 1):
            if l[j] < mini:
                mini = l[j]
                ind = j
            j += 1
        if ind == -1:
            i += 1;
            continue
        # print(ind)
        temp = ind
        while ind > i and k != 0:
            # print('ef')
            l[ind], l[ind - 1] = l[ind - 1], l[ind]
           # print(l)
            ind -= 1
            k -= 1
        i = temp
    print(*l)
