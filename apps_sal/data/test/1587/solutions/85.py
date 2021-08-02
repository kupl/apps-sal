# D
from collections import Counter
n = int(input())
c = list(input())
d = Counter(c)
# print(d)
# print(d["R"])
e = Counter(c[:d["R"]])
# print(e["R"])
print(d["R"] - e["R"])
