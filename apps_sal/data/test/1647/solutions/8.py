n = int(input())
(first, second) = (input(), input())
letters = {i: i for i in [chr(i) for i in range(ord('a'), ord('z') + 1)]}
for i in range(n):
    (s1, s2) = (first[i], second[i])
    if letters[s1] == letters[s2]:
        continue
    if s1 > s2:
        (s1, s2) = (s2, s1)
    (frm, to) = (letters[s2], letters[s1])
    for key in letters:
        if letters[key] == frm:
            letters[key] = to
result = []
for (k, v) in list(letters.items()):
    if k != v:
        result.append((k, v))
print(len(result))
for r in result:
    print(f'{r[0]} {r[1]}')
