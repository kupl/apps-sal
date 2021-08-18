n = int(input())
al = list(map(int, input().split()))

if n == 1 and al[0] == 1:
    print(0)
else:
    i, j, num, ans = 0, 0, 1, 0
    while i < n:
        if al[i] != num:
            i += 1
        else:
            ans += i - j
            j = i + 1
            num += 1
            i += 1

    if num != 1 and j != n:
        ans += i - j

    if num == 1:
        print(-1)
    else:
        print(ans)
