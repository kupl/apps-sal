for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    ans = [str(p[0])]
    for i in range(1,n-1):
        if p[i-1] < p[i] < p[i+1]:
            continue
        if p[i-1] > p[i] > p[i+1]:
            continue
        ans.append(str(p[i]))
    ans.append(str(p[-1]))
    print(len(ans))
    print(" ".join(ans))

