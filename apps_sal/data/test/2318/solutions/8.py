

t = int(input())

for test in range(t):
    s = input()
    t = input()
    arr_s = []
    arr_t = []

    prev = "1"
    for i in s:
        if i == prev:
            arr_s[-1][1] += 1
        else:
            arr_s.append([i, 1])
            prev = i

    prev = "1"
    for i in t:
        if i == prev:
            arr_t[-1][1] += 1
        else:
            arr_t.append([i, 1])
            prev = i

    ans = "YES"
    if len(arr_s) == len(arr_t):
        for i in range(len(arr_s)):
            if arr_s[i][0] == arr_t[i][0] and arr_s[i][1] <= arr_t[i][1]:
                continue
            else:
                ans = "NO"
    else:
        ans = "NO"
    print(ans)
