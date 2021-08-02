def check(k, g):
    for i in g:
        a = (i[0] + k) % n
        b = (i[1] + k) % n
        if not (min(a, b), max(a, b)) in g:
            return False
    return True


n, m = [int(i) for i in input().split()]

g = set()
for i in range(m):
    a, b = [int(i) for i in input().split()]
    a -= 1
    b -= 1
    # usar tupla ao inves de uma lista pois tuplas sao hashable
    g.add((min(a, b), max(a, b)))

for i in range(1, n):
    if n % i == 0:
        if not check(i, g):
            continue
        print('Yes')
        break
else:
    print('No')
# else depois de um for é executado se ele n quebrar
