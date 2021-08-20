t = int(input())
for you in range(t):
    n = int(input())
    freq = [0 for i in range(26)]
    for i in range(n):
        s = input()
        for x in s:
            freq[ord(x) - 97] += 1
    poss = 1
    for i in freq:
        if i % n:
            poss = 0
            break
    if poss:
        print('YES')
    else:
        print('NO')
