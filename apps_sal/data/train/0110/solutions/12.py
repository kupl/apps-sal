t = int(input())
for i in range(t):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    cnt = 0
    for j in range(k):
        if 0 < j < k - 1 and a[j - 1] < a[j] > a[j + 1]:
            cnt += 1
    ans = cnt
    l = 0
    for j in range(n - k):
        if a[j + 2] < a[j + 1] > a[j]:
            cnt -= 1
        if a[j + k - 2] < a[j + k - 1] > a[j + k]:
            cnt += 1
        if cnt > ans:
            ans = cnt
            l = j + 1
    print(ans + 1, l + 1)
