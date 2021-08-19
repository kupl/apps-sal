def resolve():
    n = int(input())
    (d, x) = map(int, input().split())
    al = list()
    ans = 0
    for i in range(n):
        a = int(input())
        al.append(a)
    cl = list()
    for i in range(n):
        counter = 1
        day = 1
        while day + al[i] <= d:
            counter += 1
            day += al[i]
        cl.append(counter)
    ans = 0
    for i in cl:
        ans += i
    ans += x
    print(ans)


resolve()
