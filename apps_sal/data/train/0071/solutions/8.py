t = int(input())
while t:
    t += -1
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    sm = 0
    for i in l:
        sm += i
        ans = min(ans, sm)
    print(abs(ans))
