N = int(input())

words = [input() for _ in range(N)]
used = [0 for _ in range(N)]


def last_vowel(s):
    for i in range(len(s) - 1, -1, -1):
        if s[i] in "aeiou":
            return s[i]
    raise RuntimeException("CF BAD")


def count_vowels(s):
    count = 0
    for c in s:
        if c in "aeiou":
            count += 1
    return count


def key(s):
    count = 0
    last = ""
    for c in s:
        if c in "aeiou":
            count += 1
            last = c
    return (count, last)


buckets = {}
finalbuckets = {}

for index, word in enumerate(words):
    k = key(word)
    if k not in buckets:
        buckets[k] = []
    if k[0] not in finalbuckets:
        finalbuckets[k[0]] = []
    buckets[k].append(index)
    finalbuckets[k[0]].append(index)

fp = []
sp = []

for b in buckets:
    if len(buckets[b]) < 2:
        continue
    for i in range(0, len(buckets[b]) - 1, 2):
        sp.append((buckets[b][i], buckets[b][i + 1]))
        used[buckets[b][i]] = 1
        used[buckets[b][i + 1]] = 1

for b in finalbuckets:
    pair = None
    for word in finalbuckets[b]:
        if used[word]:
            continue
        if pair is None:
            pair = word
        else:
            fp.append((pair, word))
            pair = None

move = max(0, (len(sp) - len(fp)) // 2)

z = list(zip(fp + sp[:move], sp[move:]))

print(len(z))

for (f0, f1), (s0, s1) in z:
    print(words[f0], words[s0])
    print(words[f1], words[s1])
