import sys
word = input()
suffixes = set()
possible = {(len(word), 2)}
my_set = set()
while possible:
    (d, x) = possible.pop()
    a = d + x
    for i in [x, 5 - x]:
        l = d - i
        q = (l, i)
        if q in my_set or l < 5 or word[l:d] == word[d:a]:
            continue
        suffixes.add(word[l:d])
        possible.add(q)
        my_set.add(q)
suffixes_alph = sorted(suffixes)
print(len(suffixes))
print(*suffixes_alph, sep='\n')
