t = int(input())
while t:
    t -= 1
    n = int(input())
    a = [int(i) for i in input().split()]
    a.reverse()
    print(*a, sep=" ")
