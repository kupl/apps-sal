# alpha = "abcdefghijklmnopqrstuvwxyz"
t = 1
for test in range(t):
    # n,s = (map(int, input().split()))
    # a = list(map(int, input().split()))
    n = int(input())
    s = input()
    ind = 0
    cur = 1
    ans = []
    while ind<n:
        ans.append(s[ind])
        ind+=cur
        cur = cur+1
    print(*ans,sep="")


