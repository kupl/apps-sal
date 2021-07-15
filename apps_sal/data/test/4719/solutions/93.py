from collections import Counter

n = int(input())
s = Counter(input())

for i in range(n-1):
    s &= Counter(input())

res = ""
for char, count in s.items():
    res += char*count
print(*sorted(res), sep="")

