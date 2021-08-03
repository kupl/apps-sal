t = int(input())
for you in range(t):
    n = int(input())
    l = input().split()
    li = [int(i) for i in l]
    if(li[0] + li[1] <= li[-1]):
        print(1, 2, n)
    else:
        print(-1)
