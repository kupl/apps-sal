for i in range(int(input())):
    num = int(input())
    data = [int(i) for i in input().split()]
    data.sort()
    k0 = min(data[-2] - 1, num - 2)
    print(max(0, k0))
