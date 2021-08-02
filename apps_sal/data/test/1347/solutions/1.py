from collections import defaultdict

input()
index = {}


def stat(word): return (word.count('r'),
                        len(word), index.setdefault(word, len(index)))


essay = list(map(stat, input().lower().split()))
queue = essay[:]

syn = defaultdict(list)
for i in range(int(input())):
    word, rep = map(stat, input().lower().split())
    syn[rep[2]].append(word[2])
    queue.append(rep)
queue.sort(reverse=True)
best = {}
while queue:
    n_r, length, word = queue.pop()
    if word in best:
        continue
    best[word] = n_r, length
    for rep in syn[word]:
        if rep not in best:
            queue.append((n_r, length, rep))
sum_n_r, sum_len = 0, 0
for n_r, length in map(lambda w: best[w[2]], essay):
    sum_n_r += n_r
    sum_len += length
print(sum_n_r, sum_len)
