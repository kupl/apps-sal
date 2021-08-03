n, k = input().split()
k = int(k)
s = sum([x == "0" for x in n])
if s < k:
    print(len(n) - 1)
else:
    res = 0
    for ch in reversed(n):
        if ch == "0":
            k -= 1
            if not k:
                break
        else:
            res += 1
    print(res)
