t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    s = input()
    prev = 0
    c = 0
    if s[0] == "0":
        c += 1
    for i, x in enumerate(s):
        if i == 0:
            continue
        if x == "1":
            if i - prev <= k:
                c -= 1
            prev = i
        else:
            if i - prev > k:
                c += 1
                prev = i
    print(c)

