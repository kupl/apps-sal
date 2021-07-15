n = int(input())
A = [int(input()) for _ in range(n)]
a = sorted(A)
i = 0
ans = 0
while i < n:
    if i == 0:
        if a[0] == a[1]:
            cnt = 2
            i = 2
            while i < n and a[i-1] == a[i]:
                cnt += 1
                i += 1
            ans += cnt%2
        else:
            ans += 1
            cnt = 1
            i = 2
            while i < n and a[i-1] == a[i]:
                cnt += 1
                i += 1
            ans += cnt%2
    else:
        cnt = 1
        i += 1
        while i < n and a[i-1] == a[i]:
            cnt += 1
            i += 1
        ans += cnt%2
print(ans)
