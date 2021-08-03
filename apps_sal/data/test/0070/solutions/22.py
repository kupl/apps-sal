l = input().split()
k = int(l[1])
n = l[0]
n = n[::-1]


def compute():
    j = 0
    i = 0
    ans = 0
    if len(n) <= k:
        return len(n) - 1
    while j < k and i < len(n):
        if n[i] != '0':
            ans += 1
        else:
            j += 1
        i += 1
    if i == len(n) and j < k:
        return len(n) - 1
    else:
        return ans


print(compute())
