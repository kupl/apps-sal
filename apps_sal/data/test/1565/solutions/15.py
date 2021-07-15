n = int(input())
s = input()

len1 = n // 2
len2 = (n + 1) // 2
S = 10**100000

def calc (d):
    nonlocal S
    h = d
    while (h < n and s[h] == '0'):
        h += 1

    if (h < n):
        S = min(S, int(s[h:]) + int(s[:h]))

    h = d
    while (0 <= h and s[h] == '0'):
        h -= 1

    if (0 < h):
        S = min(S, int(s[h:]) + int(s[:h]))

calc(len1)
calc(len2)
print(S)

