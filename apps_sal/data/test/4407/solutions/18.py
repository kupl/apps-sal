import collections
(n, q) = map(int, input().split())
s = [int(i) for i in input().split()]
a = [int(input()) for _ in range(q)]
'dic = [0] * 32\nfor key, val in collections.Counter(s).items():\n    dic[key.bit_length()-1] = val'
dic = {}
for i in range(32):
    dic[i] = 0
for i in s:
    dic[i.bit_length() - 1] += 1
for s in a:
    ans = 0
    for i in range(31, -1, -1):
        count = min(s >> i, dic[i])
        ans += count
        s -= count << i
    print(ans if s == 0 else -1)
