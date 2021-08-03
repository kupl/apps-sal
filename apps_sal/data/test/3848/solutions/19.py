def solve(s, n):
    if len(s) == 1:
        return chr(ord(s[0]) + 1) if ord(s[0]) + 1 < ord('a') + n else 'NO'

    for i in reversed(range(2, len(s))):
        c = s[i]
        for j in range(ord(c) + 1, ord('a') + n):
            next = chr(j)
            if next != s[i - 1] and next != s[i - 2]:
                new_s = s[0:i] + next
                new_s = fill(new_s, n, s, i)
                return new_s
    for i in range(ord(s[1]) + 1, ord('a') + n):
        next = chr(i)
        if next != s[0]:
            new_s = s[0] + next
            new_s = fill(new_s, n, s, 1)
            return new_s

    for i in range(ord(s[0]) + 1, ord('a') + n):
        next = chr(i)
        new_s = next
        new_s = fill(new_s, n, s, 0)
        return new_s
    return 'NO'


def fill(new_s, n, s, i):
    res = ['a', 'b', 'c']
    for x in range(i + 1, len(s)):
        for y in res:
            if ord(y) < ord('a') + n and y != new_s[-1] and (len(new_s) < 2 or y != new_s[-2]):
                new_s += y
                break
    return new_s if len(new_s) == len(s) else 'NO'


m, n = list(map(int, input().split()))
s = input()
print(solve(s, n))
