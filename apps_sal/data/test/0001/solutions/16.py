def f(n, k):
    n = str(n)
    if n[k] == "0":
        return f(n, k - 1)
    a = []
    for i in n:
        a.append(int(i))
    n = a
    n[k] = int(n[k]) - 1
    n[k + 1::] = [9] * (len(n) - k - 1)
    return n


a = input()
n = len(a)
ans = [int(x) for x in a]
ms = sum(ans)
for i in range(0, n):
    ca = f(a, i)
    cs = sum(ca)
    if cs > ms:
        ans = ca
        ms = cs
    elif cs == ms:
        if int(''.join([str(_) for _ in ca])) > int(''.join([str(_) for _ in ans])):
            ans = ca
print(int(''.join([str(_) for _ in ans])))
