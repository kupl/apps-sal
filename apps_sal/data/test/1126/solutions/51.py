from collections import defaultdict
(n, x, m) = list(map(int, input().split()))


def culc(xx, mod):
    return xx ** 2 % mod


dic = defaultdict(int)
A = x
warps = [A]
indices = [0 for i in range(m + 5)]
count = 1
circle_len = -1
tail_len = -1
while True:
    count += 1
    A = culc(A, m)
    if dic[A] >= 1:
        circle_len = count - indices[A]
        tail_len = count - circle_len - 1
        break
    warps.append(A)
    indices[A] = count
    dic[A] += 1
tail = warps[:tail_len]
circle = warps[tail_len:]
times = (n - tail_len) // circle_len
remainder = (n - tail_len) % circle_len
ans = sum(tail) + times * sum(circle) + sum(circle[:remainder])
print(ans)
