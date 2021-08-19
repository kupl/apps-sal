(n, k) = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cnt = n
while k:
    for i in range(cnt):
        print(n - cnt + 1, a[i])
        for j in range(cnt, n):
            print(a[j])
        k -= 1
        if k == 0:
            break
    cnt -= 1
