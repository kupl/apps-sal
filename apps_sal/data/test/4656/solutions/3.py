import math
t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    s = input()
    countLetters = [0] * 26
    for elem in s:
        countLetters[ord(elem) - ord('a')] += 1
    factors = []
    for i in range(1, int(math.sqrt(k)) + 1):
        if k % i == 0:
            factors.append(i)
            factors.append(k // i)
    groups = []
    for i in range(1, n + 1):
        sumBeads = 0
        for elem in countLetters:
            sumBeads += elem // i
        groups.append(sumBeads)
    maxNecklace = 0
    for elem in factors:
        maxGroup = 0
        for i in range(n):
            if groups[i] < elem:
                break
            else:
                maxGroup = i + 1
        if maxNecklace < maxGroup * elem:
            maxNecklace = maxGroup * elem
    print(maxNecklace)
