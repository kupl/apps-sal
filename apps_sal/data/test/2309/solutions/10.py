GL = set(list('aeiou'))
n = int(input())
di = dict()
tails = dict()
ends = 0
ends_words = []
starts = 0
starts_words = []
for i in range(n):
    word = input()
    counter = 0
    for w in word:
        if w in GL:
            last = w
            counter += 1
    if (last, counter) not in di:
        di[last, counter] = [word]
    else:
        di[last, counter].append(word)
for i in list(di.keys()):
    ends += len(di[i]) // 2 * 2
    while len(di[i]) > 1:
        fir = di[i].pop()
        sec = di[i].pop()
        ends_words.append([fir, sec])
for i in list(di.keys()):
    if di[i] == []:
        continue
    if i[1] in tails:
        starts += 2
        starts_words.append([di[i][0], tails[i[1]]])
        del tails[i[1]]
    else:
        tails[i[1]] = di[i][0]
while len(ends_words) > len(starts_words):
    starts_words.append(ends_words.pop())
print(len(ends_words))
for i in range(len(ends_words)):
    end = ends_words.pop()
    st = starts_words.pop()
    print(st[0], end[0])
    print(st[1], end[1])
