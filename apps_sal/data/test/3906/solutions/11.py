
width, height = list(map(int, input().strip().split(' ')[:2]))

modulo = 10**9 + 7
fibs = [0, 0]
sum_fibs = [0, 0]
a, b = 1, 0
for i in range(max(width, height)):
    fibs.append(a)
    sum_fibs.append((sum_fibs[-1] + a) % modulo)
    a, b = (a + b) % modulo, a


def ans(w, h):
    return 2 * (1 + sum_fibs[w] + sum_fibs[h]) % modulo


print(ans(width, height))
