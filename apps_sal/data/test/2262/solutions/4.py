n = int(input())
s = set()
w = [frozenset(x) for x in input().split()]
for i in range(n):
    s.add(w[i])
print(len(s))
