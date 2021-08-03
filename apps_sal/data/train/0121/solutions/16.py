for t in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    l.sort()
    print(abs(l[n] - l[n - 1]))
