n = int(input())
s = list(input())
t = list(input())
if sorted(s) != sorted(t):
    print(-1)
else:
    steps = []
    for i in range(n):
        needed = i
        for j in range(i, n):
            if s[j] == t[i]:
                needed = j
                break
        while needed > i:
            steps.append(needed)
            needed -= 1
            (s[needed], s[needed + 1]) = (s[needed + 1], s[needed])
    print(len(steps))
    print(' '.join(map(str, steps)))
