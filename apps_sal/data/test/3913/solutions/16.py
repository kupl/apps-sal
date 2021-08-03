import string
m = int(input())
word = input()
words = set()
stars = set()
let = {a for a in string.ascii_lowercase}
for i in range(0, len(word)):
    if word[i] == '*':
        stars.add(i)
    else:
        words.add(word[i])

n = int(input())
tse = set()
for i in range(0, n):
    st = input()
    for j in stars:
        tse.add(st[j])
    flag = True
    j = 0
    while j < m and (st[j] == word[j] or j in stars):
        j += 1

    if len(tse.intersection(words)) != 0 or j != m:
        tse.clear()
        continue
    let = let.intersection(tse)
    tse.clear()

if len(stars) == 0:
    print(0)
else:
    print(len(let))
