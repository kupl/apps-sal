def gen_graph(i, step, L):
    # index iから始める
    # 0からweight*(L-1)までのL種の長さを作る
    if L == 1:
        return [i], []
    v, e = gen_graph(i + 1, 2 * step, L // 2)
    v = [i] + v
    e = e + [(i, i + 1, 0), (i, i + 1, step)]
    # (0 or 1)+(L//2種の偶数)が作れている
    if L % 2 == 0:
        return v, e
    e.append((i, v[-1], step * (L - 1)))
    return v, e


L = int(input())

v, e = gen_graph(1, 1, L)
print((len(v), len(e)))
for a, b, c in e:
    print((a, b, c))
