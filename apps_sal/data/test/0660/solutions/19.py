import queue
import math
import io


s = [2, 4, 8, 16, 32, 64, 128, 256, 512]


def step(n):
    st = 0
    for i in range(len(s)):
        if(s[i] > n):
            st = s[i - 1]
            break
    return [(n - st) + st // 2, st // 2]


[n, b, p] = [int(x) for x in input().split(' ')]
res = 0
res_p = n * p
while n > 1:
    [n, rb] = step(n)
    res += rb * 2 * b + rb
print(str(res) + " " + str(res_p))
