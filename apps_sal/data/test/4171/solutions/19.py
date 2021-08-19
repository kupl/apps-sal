def deep(mas, pref, k):
    deepmas = []
    s = 0
    for el in mas:
        if el[:len(pref)] == pref:
            deepmas.append(el)
            if len(deepmas) <= k:
                s += len(el) - len(pref)
    if len(deepmas) >= k:
        return min(s, deep(deepmas, pref + '0', k), deep(deepmas, pref + '1', k))
    else:
        return 20000000000000000


(n, k) = list(map(int, input().split()))
mas = list(map(int, input().split()))
mas.sort()
mas = list(map(bin, mas))
pref = '0b'
ans = deep(mas, pref, k)
print(ans)
