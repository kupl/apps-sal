for nt in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    if n == 1:
        print(abs(l[0] - l[1]))
        continue
    l.sort()
    print(abs(l[n] - l[n - 1]))
