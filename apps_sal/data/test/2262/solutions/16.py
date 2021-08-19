n = int(input())
words = set()
ss = input().split()
for s in ss:
    w = frozenset(s)
    words.add(w)
print(len(words))
