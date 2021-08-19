t = int(input())
for i in range(t):
    (n, a, b) = list(map(int, input().split()))
    s = input()
    arr = []
    c = '0'
    k = 0
    for i in range(n):
        if s[i] == c:
            k += 1
        else:
            arr.append(k)
            k = 1
            c = s[i]
    if len(arr) == 0:
        print(n * a + b * n + b)
    else:
        ans = k * (a + b) + (a + b) * arr[0] + a
        for i in range(1, len(arr)):
            if i % 2 == 1:
                ans += (arr[i] + 1) * (2 * b + a)
            else:
                ans += min((arr[i] + 1) * a + b * (arr[i] - 1), 2 * b * (arr[i] - 1) + a * (arr[i] - 1))
        print(ans)
