w = int(input())


def fun(x, n):
    if x % n != 0:
        return x % n
    else:
        return n


for we in range(w):
    n = int(input())
    l = list(map(int, input().split()))
    if n == 1:
        print("YES")
    else:
        start = l[0]
        odp = 1
        if l[1] == fun(l[0] + 1, n):
            for i in range(1, n):
                if l[i] != fun(l[i - 1] + 1, n):
                    odp = 0
                    break
        elif l[1] == fun(l[0] - 1, n):
            for i in range(1, n):
                if l[i] != fun(l[i - 1] - 1, n):
                    odp = 0
                    break
        else:
            odp = 0
        if odp == 0:
            print("NO")
        else:
            print("YES")
