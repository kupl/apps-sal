T = int(input())
for test in range(T):
    n, t = list(map(int, input().split()))
    a = list(map(int, input().split()))
    res = []
    j = 0
    for i in a:
        if(i * 2 < t):
            res += ["0"]
        elif(i * 2 > t):
            res += ["1"]
        else:
            res.append(["0", "1"][j])
            j = 1 - j
    print(" ".join(res))
