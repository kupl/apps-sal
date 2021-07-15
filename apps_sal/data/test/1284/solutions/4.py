def getsum(a, b, pref):
    if b < a:
        b += n
    return pref[b] - pref[a]


for _ in range(1):
    # for _ in range(int(input())):
    # a, b = map(int, input().split())
    n = int(input())
    arr = list(map(int, input().split()))
    # s = input()
    pref0 = [0] * (len(arr) + 1)
    pref1 = [0] * (len(arr) + 1)
    for i in range(1, len(pref0)):
        pref0[i] = pref0[i - 1]
        pref1[i] = pref1[i - 1]
        if i % 2 == 1:
            pref0[i] += arr[i - 1]
        else:
            pref1[i] += arr[i - 1]
    mx = pref0[-1]
    s = sum(arr)
    for i in range(n - 1):
        if i % 2 == 0:
            x = pref0[i + 1] + (s - pref0[-1] - pref1[i + 1])
        else:
            x = pref1[i + 1] + (s - pref1[-1] - pref0[i + 1])
        mx = max(mx, x)
    print(mx)
