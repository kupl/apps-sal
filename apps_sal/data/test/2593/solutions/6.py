for t in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    d = dict()
    for i in range(39):
        d[i] = 0
    for i in x:
        num = len(str(bin(i)))
        d[num] += 1
    ans = 0
    for s in d:
        ans += (d[s] * (d[s] - 1) // 2)
    print(ans)
