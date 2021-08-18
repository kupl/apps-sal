from collections import Counter
n = int(input())
c = list(input())
d = Counter(c)
e = Counter(c[:d["R"]])
print(d["R"] - e["R"])
