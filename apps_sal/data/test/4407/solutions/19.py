import collections
n, q = map(int, input().split())
l = list(map(int, input().split()))
a = [int(input()) for _ in range(q)]
count = [0] * 31
for key, val in collections.Counter(l).items():
    count[key.bit_length() - 1] = val
for x in a:
    ans = 0
    for i in range(30, -1, -1):
        val = min(x >> i, count[i])
        ans += val
        x -= (1 << i) * val
    print(ans if x == 0 else -1)
