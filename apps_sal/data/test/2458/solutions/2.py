from sys import stdin, stdout
lines = list([_f for _f in stdin.read().split('\n') if _f])


def parseline(line):
    return list(map(int, line.split()))


lines = list(map(parseline, lines))
(t, k) = lines[0]
assert len(lines) >= t + 1
max_flowers = 10 ** 5
modulo = 10 ** 9 + 7
A = [0] * (1 + max_flowers)
A[0] = 1
A_sum = [0] * (1 + max_flowers)
for i in range(1, 1 + max_flowers):
    Ai_m_k = A[i - k] if i >= k else 0
    A[i] = (A[i - 1] + Ai_m_k) % modulo
    A_sum[i] = (A_sum[i - 1] + A[i]) % modulo


def tests():
    for i in range(1, t + 1):
        yield lines[i]


for (a, b) in tests():
    print((A_sum[b] - A_sum[a - 1]) % modulo)
