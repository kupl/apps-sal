n, k = input().split()
k = int(k)
cnt = 0
for i in n:
    if i == "0":
        cnt += 1
if cnt < k:
    print(len(n) - 1)
else:
    p = 0
    ans = 0
    i = len(n) - 1
    while ans < k:
        if n[i] == "0":
            ans += 1
        else:
            p += 1
        i -= 1
    print(p)
