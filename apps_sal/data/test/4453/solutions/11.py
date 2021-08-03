for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= 1
    for i in range(n):
        ans = 0
        x = a[i]
        while x != i:
            ans += 1
            x = a[x]
        print(ans + 1, end=" ")
    print()
