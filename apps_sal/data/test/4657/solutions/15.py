from sys import stdin
input = stdin.readline
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if a[i] & 1:
            ans.append(i + 1)
    if len(ans) < k:
        print("NO")
    elif (k - len(ans)) & 1:
        print("NO")
    else:
        print("YES")
        ans[-1] = n
        print(*ans[len(ans) - k:])
