import math


def ones(n):
    number_of_bits = int(math.floor(math.log(n) / math.log(2))) + 1
    return [(1 << number_of_bits) - 1 ^ n, (1 << number_of_bits) - 1]


n = int(input())
has = [0] * (n + 1)
ans = [0] * (n + 1)
fin = 0
for i in range(n, 0, -1):
    if has[i] == 0:
        (com, fi) = ones(i)
        has[com] = 1
        fin += 2 * fi
        ans[com] = i
        ans[i] = com
print(fin)
print(*ans)
