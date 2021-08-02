from itertools import groupby
for _ in range(int(input())):
    s = input()
    n = len(s)
    i = j = 0
    while i < n or j < n:
        while i < n and int(s[i]) % 2:
            i += 1
        while j < n and not int(s[j]) % 2:
            j += 1
        if i == j == n:
            break
        if i < n and (j == n or s[i] < s[j]):
            print(end=s[i])
            i += 1
        else:
            print(end=s[j])
            j += 1
    print()
