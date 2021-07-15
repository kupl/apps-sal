n = int(input())
from collections import Counter
c = Counter()
for _ in range(n):
    s = input()[0]
    c[s] += 1

ans = 0
ans += c["M"]*c["A"]*c["R"]
ans += c["M"]*c["A"]*c["C"]
ans += c["M"]*c["A"]*c["H"]
ans += c["M"]*c["R"]*c["C"]
ans += c["M"]*c["R"]*c["H"]
ans += c["M"]*c["C"]*c["H"]
ans += c["A"]*c["R"]*c["C"]
ans += c["A"]*c["R"]*c["H"]
ans += c["A"]*c["C"]*c["H"]
ans += c["R"]*c["C"]*c["H"]

print(ans)
