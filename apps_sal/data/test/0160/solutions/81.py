def divisor(n):
    ass = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            ass.append(i)
            if i != n // i:
                ass.append(n // i)
    return ass


_, k = map(int, input().split())
a = list(map(int, input().split()))
for ans in sorted(divisor(sum(a)))[::-1]:
    b = [i % ans for i in a if i % ans]
    n = len(b)
    b.sort()
    m = [0] + [i for i in b]
    p = [ans - i for i in b] + [0]
    for i in range(n):
        m[i + 1] += m[i]
        p[-i - 2] += p[-i - 1]
    flag = False
    for i in range(n + 1):
        if max(m[i], p[i]) > k:
            continue
        if abs(m[i] - p[i]) % ans != 0:
            continue
        flag = True
    if flag:
        print(ans)
        return
