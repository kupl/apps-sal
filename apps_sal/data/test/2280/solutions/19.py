t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    a.sort()
    maxK = a[-2]-1
    ans = min(maxK,len(a)-2)
    print(ans)
