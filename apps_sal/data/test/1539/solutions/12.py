def f():
    return map(int, input().split())


(k, n) = (1, f())
s = sorted(zip(f(), f()), key=lambda q: q[0])
t = [0] * 201
for (l, d) in s:
    t[d] += 1
j = [i for i in range(201) if t[i]]
j.reverse()
S = sum((i * t[i] for i in j))
(L, D) = s.pop()
t[D] -= 1
s.reverse()
s.append((0, 0))
m = 0
for (l, d) in s:
    if l < L:
        L = l
        for i in j:
            if t[i] > k - 2:
                D += i * (k - 1)
                break
            D += i * t[i]
            k -= t[i]
        m = max(m, D)
        k = D = 0
    k += 1
    D += d
    t[d] -= 1
    if not t[d]:
        j.remove(d)
print(S - m)
