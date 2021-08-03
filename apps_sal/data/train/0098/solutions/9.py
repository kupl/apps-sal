n = int(input())
while n:
    n -= 1
    l = list(map(int, input().split()))
    if sum(l) // 3 < min(l[0], l[1]):
        print(sum(l) // 3)
    else:
        print(min(l[0], l[1]))
