import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
N = int(input())
words = [input()[:-1] for _ in range(N)]
vowels = ('a', 'i', 'u', 'e', 'o')
counted_word = []
for word in words:
    last_vowel = ''
    num_vowel = 0
    for c in word:
        if c in vowels:
            num_vowel += 1
            last_vowel = c
    counted_word.append([word, num_vowel, last_vowel])
counted_word = sorted(counted_word, key=lambda x: (x[1], x[2]))
cand_second = []
unused = []
used = [False] * N
for (i, w1, w2) in zip(list(range(N)), counted_word, counted_word[1:]):
    if used[i]:
        continue
    if w1[1] == w2[1] and w1[2] == w2[2]:
        cand_second.append([w1, w2])
        used[i] = True
        used[i + 1] = True
    else:
        unused.append(w1)
if not used[-1]:
    unused.append(counted_word[-1])
cand_first = []
used = [0] * len(unused)
for (i, w1, w2) in zip(list(range(len(unused))), unused, unused[1:]):
    if used[i]:
        continue
    if w1[1] == w2[1]:
        cand_first.append([w1, w2])
        used[i] = True
        used[i + 1] = True
len_first = len(cand_first)
len_second = len(cand_second)
diff = len_second - len_first
if diff > 1:
    for i in range(diff // 2):
        cand_first.append(cand_second[-i - 1])
ans = min(len_second, len(cand_first))
print(ans)
for (first, second) in zip(cand_first, cand_second):
    print(first[0][0], second[0][0])
    print(first[1][0], second[1][0])
