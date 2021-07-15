for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    c = a.count(0)
    summ = sum(a)
    if c > 0:
        ans += c
        summ += c
    if summ == 0:
        ans += 1
    print(ans)
