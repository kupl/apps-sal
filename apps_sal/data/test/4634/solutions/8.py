for __ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ans = ar.count(0)
    i = 0
    while ar[i] == 0:
        ans -= 1
        i += 1
    j = n - 1
    while ar[j] == 0 and i != j:
        ans -= 1
        j -= 1
    print(max(0, ans))
