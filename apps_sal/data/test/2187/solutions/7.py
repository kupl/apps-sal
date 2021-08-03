t = int(input())
for you in range(t):
    n = int(input())
    l = input().split()
    li = [int(i) for i in l]
    curr = 0
    for i in range(1, n):
        if(li[i] < li[i - 1]):
            curr = curr + (li[i - 1] - li[i])
    print(curr)
