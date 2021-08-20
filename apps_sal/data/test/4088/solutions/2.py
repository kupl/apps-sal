for _ in range(int(input())):
    s = input()
    m = int(input())
    b = list(map(int, input().split()))
    values = {}
    for num in b:
        if num not in values:
            values[num] = 0
        values[num] += 1
    letters = {}
    for c in s:
        if c not in letters:
            letters[c] = 0
        letters[c] += 1
    sortedLetters = []
    sortedValues = []
    for elem in letters:
        sortedLetters.append((elem, letters[elem]))
    sortedLetters.sort()
    ans = ['' for _ in range(m)]
    while True:
        done = True
        toChange = []
        for i in range(m):
            dist = 0
            if ans[i] != '':
                continue
            for j in range(m):
                if ans[j] != '':
                    dist += abs(i - j)
            if dist == b[i]:
                toChange.append(i)
        if len(toChange) == 0:
            break
        cnt = len(toChange)
        while sortedLetters[-1][1] < cnt:
            sortedLetters.pop(-1)
        for i in toChange:
            ans[i] = sortedLetters[-1][0]
        sortedLetters.pop(-1)
    print(''.join(ans))
