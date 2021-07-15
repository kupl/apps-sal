def main():
    N, K  = [int(i) for i in input().split()]
    A  = [int(i) for i in input().split()]
    v = {0: 1}
    n = [0]
    r = 0
    t = 0
    for i, a in enumerate(A, 1):
        if i >= K:
            v[n[i - K]] -= 1
        t += a
        j = (t - i) % K
        r += v.get(j, 0)
        v[j] = v.get(j, 0) + 1
        n.append(j)

    return r


print((main()))

