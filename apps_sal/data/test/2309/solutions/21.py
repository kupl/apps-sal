first_pairs = []
second_pairs = []
lines = int(input())
words = {}
for i in range(lines):
    w = input()
    vow_cnt = 0
    vow_last = ''
    for c in w:
        if c in ['a', 'e', 'i', 'o', 'u']:
            vow_cnt += 1
            vow_last = c
    if vow_cnt not in words:
        words[vow_cnt] = {}
    if vow_last not in words[vow_cnt]:
        words[vow_cnt][vow_last] = w
    else:
        second_pairs.append((words[vow_cnt][vow_last], w))
        del words[vow_cnt][vow_last]
for l in words:
    first = None
    second = None
    for k in list(words[l].keys()):
        if first is None:
            first = k
            continue
        second = k
        first_pairs.append((words[l][first], words[l][second]))
        first = None
while len(first_pairs) < len(second_pairs):
    first_pairs.append(second_pairs.pop())
print(len(second_pairs))
for (f, s) in zip(first_pairs, second_pairs):
    print('{} {}'.format(f[0], s[0]))
    print('{} {}'.format(f[1], s[1]))
