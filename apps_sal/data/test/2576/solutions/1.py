def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s)]))


def invr():
    return(list(map(int, input().split())))


n = inp()

for _ in range(n):
    l = inlt()

    a = l[0]
    b = l[1]
    c = l[2]
    d = l[3]

    if(a + b > c + d):
        print(a + b)
    else:
        print(c + d)
