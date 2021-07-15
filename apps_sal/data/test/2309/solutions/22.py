from collections import defaultdict

vow = "aeoiu"


def vowels(word):
    c = 0
    for i in word:
        if i in vow:
            c += 1
    return c


def last_vov(word):
    for i in reversed(word):
        if i in vow:
            return i


mp = defaultdict(lambda: defaultdict(list))

for _ in range(int(input())):
    w = input()
    mp[vowels(w)][last_vov(w)].append(w)

second_w = []
first_w = []

for last_v_dict in mp.values():
    first_w_t = []
    for words in last_v_dict.values():
        if len(words) % 2 == 1:
            if len(words) > 2:
                second_w += words[:-1]
            first_w_t.append(words[-1])
        else:
            second_w += words
    if len(first_w_t) >= 2:
        if len(first_w_t) % 2 == 1:
            first_w += first_w_t[:-1]
        else:
            first_w += first_w_t

while len(second_w) > len(first_w):
    first_w.append(second_w.pop())
    first_w.append(second_w.pop())

print(len(second_w) // 2)
for i, word in enumerate(second_w):
    print(first_w[i], word)
