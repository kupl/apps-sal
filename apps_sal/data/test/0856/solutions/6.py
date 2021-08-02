t = int(input())
for you in range(t):
    l = input().split()
    n = int(l[0])
    k = int(l[1])
    l = input().split()
    li = [int(i) for i in l]
    x = min(li)
    y = max(li)
    if(k % 2):
        for i in li:
            print(y - i, end=" ")
        print()
    else:
        for i in li:
            print(i - x, end=" ")
        print()
