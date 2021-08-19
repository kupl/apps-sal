from collections import Counter
import math
n, a, b = map(int, input().split())
v = sorted(list(map(int, input().split())))[::-1]
l = Counter(v)
su = 0
ko = 0


def C(a, b):
    return math.factorial(a) // (math.factorial(b) * math.factorial(a - b))


for i in range(a, b + 1):
    v1 = v[:i]
    s = sum(v1) / i
    if su < s:
        su = s
        ko = C(l[v[a]], v1.count(v1[-1]))
    elif su == s:
        ko += C(l[v[a]], v1.count(v1[-1]))
     # print(s,ko)
print(su)
print(ko)
