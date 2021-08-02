q = int(input())
for re in range(q):
    n = int(input())
    l = list(map(int, input().split()))
    pref = [0] * n
    pref[0] = l[0]
    for i in range(1, n):
        pref[i] = pref[i - 1] + l[i]
    prefr = [0] * n
    prefr[0] = l[n - 1]
    for i in range(1, n):
        prefr[i] = prefr[i - 1] + l[n - i - 1]
    odp = 1
    for i in range(n):
        if prefr[i] <= 0:
            odp = 0
            break
    for i in range(n):
        if pref[i] <= 0:
            odp = 0
            break
    if odp:
        print("YES")
    else:
        print("NO")
