from collections import Counter

N = int(input())
C = [Counter(input()) for _ in range(N)]

word_set = set(C[0].keys())
for c in C:
    word_set &= set(list(c.keys()))

W = {key: 10**8 for key in word_set}
for c in C:
    for word in word_set:
        W[word] = min(W.get(word, 0), c.get(word, 0))

ans = ''
for key, value in list(W.items()):
    ans += key * value
print((''.join(sorted(ans))))
