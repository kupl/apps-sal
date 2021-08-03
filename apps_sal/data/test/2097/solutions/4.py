for nt in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if l[i] == 0:
            count += 1
            l[i] = 1
    if sum(l) == 0:
        count += 1
    print(count)
