def counts(n: int):
    if n % 2 == 0:
        return (n ** 2 // 2, n ** 2 // 2)
    return (n ** 2 // 2, n ** 2 - n ** 2 // 2)


(soft, hard) = (0, 0)
n = int(input())
for _ in range(n):
    (_, typ) = input().split()
    if typ == 'soft':
        soft += 1
    else:
        hard += 1


def solve(soft, hard):
    for k in range(1, 1000):
        (max_white, max_black) = counts(k)
        if soft <= max_white and hard <= max_black or (soft <= max_black and hard <= max_white):
            return k


print(solve(soft, hard))
