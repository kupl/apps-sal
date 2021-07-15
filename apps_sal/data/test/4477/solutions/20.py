for _ in range(int(input())):
    n = input()
    c = int(n[0])
    ans = (c - 1) * 10
    k = len(n)
    for i in range(1, k + 1):
        ans += i
    print(ans)
