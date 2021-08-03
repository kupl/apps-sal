for t in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        l += list(input())

    ans = 'YES'
    for i in l:
        if l.count(i) % n != 0:
            ans = 'NO'

    print(ans)
