from bisect import *
strings = []
zeronumber = []
for i in range(1, 200001):
    strings.append(format(i, "b"))
    zeronumber.append(i - i.bit_length())

t = int(input())
for _ in range(t):
    s = input()
    z = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == "0":
            z += 1
            continue
        else:
            for j in range(bisect_right(zeronumber, z)):
                if i + len(strings[j]) - 1 <= len(s) - 1:
                    if s[i:i + len(strings[j])] == strings[j]:
                        ans += 1
            z = 0
    print(ans)
