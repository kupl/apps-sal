n, m, i, j, a, b = map(int, input().split())
def Good(i, a, n, d): return None if abs(i - d) % a != 0 else (abs(i - d) // a % 2 if abs(i - d) // a >= 1 else (0 if i + a <= n or i - a >= 1 else -1))


res = None
xx, yy = [1, n], [1, m]
for dx in xx:
    for dy in yy:
        tx, ty = Good(i, a, n, dx), Good(j, b, m, dy)
        if tx is None or ty is None:
            continue
        if tx == -1 or ty == -1:
            if (tx == -1 and abs(j - dy) // b == 0) or (ty == -1 and abs(i - dx) // a == 0):
                res = 0
            continue
        if tx != ty:
            continue
        new_res = max(abs(i - dx) // a, abs(j - dy) // b)
        res = new_res if res is None or res > new_res else res
print('Poor Inna and pony!' if res is None else res)
