import sys


def main():
    #n = iinput()
    #k = iinput()
    #m = iinput()
    #n = int(sys.stdin.readline().strip())
    #n, k = rinput()
    #n, m = rinput()
    #m, k = rinput()
    #n, k, m = rinput()
    #n, m, k = rinput()
    #k, n, m = rinput()
    #k, m, n = rinput()
    #m, k, n = rinput()
    #m, n, k = rinput()
    #n, t = map(int, sys.stdin.readline().split())
    #q = list(map(int, sys.stdin.readline().split()))
    #q = linput()
    n, m = list(map(int, sys.stdin.readline().split()))
    q = []
    for i in range(n):
        q.append([list(map(int, sys.stdin.readline().split())), list(map(int, sys.stdin.readline().split()))])
    if m % 2:
        print("NO")
    else:
        fl = 0
        for i in range(n):
            if q[i][0][1] == q[i][1][0]:
                fl = 1
                break
        if fl:
            print("YES")
        else:
            print("NO")


for i in range(int(sys.stdin.readline().strip())):
    main()
