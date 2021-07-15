for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    z = a.count(0)
    j = 0
    while j < n and a[j] != 1:
        j += 1
        z -= 1
    j = n - 1
    while j >= 0 and a[j] != 1:
        j -= 1
        z -= 1    
    print(z)
