for __ in range(int(input())):
    n = int(input())
    ar1 = list(map(int, input().split()))
    ar2 = list(map(int, input().split()))
    ar3 = list(map(int, input().split()))
    ans = [ar1[0]]
    for i in range(1, n - 1):
        if ar1[i] != ans[-1]:
            ans.append(ar1[i])
        elif ar2[i] != ans[-1]:
            ans.append(ar2[i])
        elif ar3[i] != ans[-1]:
            ans.append(ar3[i])
    if ar1[-1] != ans[-1] and ar1[-1] != ans[0]:
        ans.append(ar1[-1])
    elif ar2[-1] != ans[-1] and ar2[-1] != ans[0]:
        ans.append(ar2[-1])
    elif ar3[-1] != ans[-1] and ar3[-1] != ans[0]:
        ans.append(ar3[-1])
    print(*ans)
