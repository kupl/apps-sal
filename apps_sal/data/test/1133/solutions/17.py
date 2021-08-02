n = int(input())
c = [[0] * 26 for i in range(26)]
for w in range(n):
    word = input()
    wset = list(set(word))
    wset[0] = ord(wset[0]) - ord('a')
    if len(wset) > 1:
        wset[1] = ord(wset[1]) - ord('a')
    if len(wset) == 2:
        c[wset[0]][wset[1]] += len(word)
        c[wset[1]][wset[0]] += len(word)
    if len(wset) == 1:
        for i in range(26):
            c[i][wset[0]] += len(word)
            c[wset[0]][i] += len(word)
            c[wset[0]][wset[0]] -= len(word)
print(max([max(c[i]) for i in range(26)]))
