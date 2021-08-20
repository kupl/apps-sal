(s, t) = (input(), input())
(i, j) = (len(s) - 1, len(t) - 1)
x = 0
while i != -1 and j != -1:
    if s[i] != t[j]:
        break
    x += 1
    i -= 1
    j -= 1
print(len(s) + len(t) - 2 * x)
