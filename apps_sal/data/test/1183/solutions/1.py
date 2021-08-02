t = int(input())
for _ in range(t):
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    d = dict()
    for i in arr:
        d[i] = 1
    ans = 0
    for i in range(1, 202):
        if(i in d):
            ans += 1
        elif(x > 0):
            x -= 1
            ans += 1
        else:
            break
    print(ans)
