for _ in range(int(input())):
    s = input()
    n = len(s)
    i = 0
    valid = set()
    while i < n:
        j = i + 1
        while j < n and s[j] == s[i]: j += 1
        if (j - i) & 1: valid.add(s[i])
        i = j
    print(''.join(sorted(valid)))
