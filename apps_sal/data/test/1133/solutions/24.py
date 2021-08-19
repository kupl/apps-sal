def valid(w, a, b):
    for i in w:
        if i not in [a, b]:
            return False
    return True


n = int(input())
words = []
for i in range(n):
    s = input()
    words.append(s)
maxi = 0
for i in range(26):
    for j in range(26):
        (a, b) = (chr(97 + i), chr(97 + j))
        cur = 0
        for w in words:
            if valid(w, a, b):
                cur += len(w)
        if cur > maxi:
            maxi = cur
print(maxi)
