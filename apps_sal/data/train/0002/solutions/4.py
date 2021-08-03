gans = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = [a[0]]
    for i in range(1, n - 1):
        if a[i] != ans[i - 1]:
            ans.append(a[i])
        else:
            ans.append(b[i])
    if a[-1] != ans[-1] and a[-1] != ans[0]:
        ans.append(a[-1])
    elif b[-1] != ans[-1] and b[-1] != ans[0]:
        ans.append(b[-1])
    else:
        ans.append(c[-1])
    gans.append(' '.join(map(str, ans)))
print('\n'.join(gans))
