
N, A, B = list(map(int, input().split()))
v = list(map(int, input().split()))

v = sorted(v)[::-1]

v_ref = sum(v[:A])

i = A
n_min = A
n_max = B
while (i < B):
    v_new = v_ref + v[i]
    if i * v_new < (i + 1) * v_ref:
        n_max = i
        break
    if i * v_new > (i + 1) * v_ref:
        n_min = i + 1
    v_ref = v_new
    i += 1


def comb(n, k):
    r = 1
    for x, y in zip(list(range(n, n - k, -1)), list(range(1, k + 1))):
        r = r * x
        assert r % y == 0
        r = r // y
    return r


result = 0
for n in range(n_min, n_max + 1):
    v_min = min(v[:n])
    num_min = sum([v_ == v_min for v_ in v])
    num_fixed = sum([v_ > v_min for v_ in v[:n]])
    num_selected = n - num_fixed
    result += comb(num_min, num_selected)

v_max_avg = sum(v[:n_min]) / n_min

print(f"{v_max_avg:.6f}")
print(result)
