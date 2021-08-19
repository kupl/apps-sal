import sys
input = sys.stdin.readline


def mii():
    return list(map(int, input().split()))


s = input().strip()
d = [0] * 1000
e = [0] * 1000
hist = [0] * 26
for i in s:
    j = ord(i) - ord('a')
    for k in range(26):
        e[k * 26 + j] += hist[k]
    hist[j] += 1
    d[j] += 1
print(max(d + e))
