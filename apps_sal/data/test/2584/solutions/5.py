t = int(input())
for i in range(0, t):
    n, p, k = list(map(int, input().split()))
    q = [int(x) for x in input().split()]
    q = sorted(q)
    if p < q[0]:
        print(0)
    else:
        if n == 1:
            print(1)
        elif n == 2:
            if p >= q[1]:
                print(2)
            else:
                print(1)
        else:
            j = 1
            s = 0
            y = p
            k = 1
            x = 1
            while 2 * j - 1 <= n - 1:
                if p >= q[2 * j - 1]:
                    p -= q[2 * j - 1]
                    s += 2
                else:
                    if p >= q[2 * j - 2]:
                        s += 1
                    break
                j += 1
            y -= q[0]
            while 2 * k <= n - 1:
                if y >= q[2 * k]:
                    y -= q[2 * k]
                    x += 2
                else:
                    if y >= q[2 * k - 1]:
                        x += 1
                    break
                k += 1
            print(max(s, x))
