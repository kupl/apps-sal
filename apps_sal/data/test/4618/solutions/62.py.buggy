s = input()
k = int(input())

alphabets = [chr(i + 97) for i in range(26)]

for char in alphabets:
    l = []
    for i in range(len(s)):
        if s[i] == char:
            l.append(s[i:])

    if l == []:
        continue

    if k == 1:
        print((l[0][0]))
        return

    k -= 1

    strings = set([])
    for i in l:
        for j in range(2, min(k + 2, len(i) + 1)):
            strings.add(i[:j])
    strings = list(strings)
    strings.sort()

    if len(strings) >= k:
        print((strings[k - 1]))
        return
    else:
        k -= len(strings)
