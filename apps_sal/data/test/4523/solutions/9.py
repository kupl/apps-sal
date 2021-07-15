for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    ans = "YES"
    for i in range(n-1):
        if lst[i+1]-lst[i]>1:
            ans = "NO"
            break
    print(ans)
