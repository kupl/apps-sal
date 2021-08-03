n, t = map(int, input().split())
l = list(map(int, input().split()))
ma = j = k = kt = 0
for i in range(n):
    if l[i] + kt <= t:
        k += 1
        kt += l[i]
        if ma < k:
            ma = k
    else:
        while l[i] + kt > t:
            if k == 0:
                j = i + 1
                break
            kt -= l[j]
            k -= 1
            j += 1
        if kt + l[i] <= t:
            k += 1
            kt += l[i]
            if ma < k:
                ma = k
print(ma)
