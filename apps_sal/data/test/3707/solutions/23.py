import math

n, t, k, d = list(map(int, input().split()))

time = t * math.ceil(n / k)
cnt = ((time - 1) // t + max(0, time - 1 - d) // t) * k

print('YES' if cnt >= n else 'NO')
