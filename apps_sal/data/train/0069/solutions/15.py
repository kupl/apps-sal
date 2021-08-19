t = int(input())
for _ in range(t):
    (a, b) = list(map(int, input().split()))
    s = input()
    n = len(s)
    ind1 = 0
    ind2 = n - 1
    while ind1 != n and s[ind1] == '0':
        ind1 += 1
    while ind2 != -1 and s[ind2] == '0':
        ind2 -= 1
    if ind1 == n:
        print(0)
        continue
    arr = []
    count = 0
    for i in range(ind1, ind2 + 1):
        if s[i] == '0':
            count += 1
        else:
            if count != 0:
                arr += [count]
            count = 0
    if count != 0:
        arr += [count]
    ans = a * (len(arr) + 1)
    arr.sort()
    tot = 0
    for i in range(len(arr)):
        tot += arr[i]
        ans = min(ans, b * tot + a * (len(arr) - i))
    print(ans)
