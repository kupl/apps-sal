def yoba(a, k):
    if not a:
        return []
    elif not k:
        return a
    else:
        m = max(a[:k + 1])
        mi = a.index(m)
        if m > a[0]:
            a[1:mi + 1] = a[:mi]
            a[0] = m
            k -= mi
        return [a[0]] + yoba(a[1:], k)


(a, k) = str.split(input())
k = int(k)
print(str.join('', yoba(list(a), k)))
