
s = str(input())
k = int(input())


a = 0


def tandem(string):
    if len(string) % 2 == 1:
        return False
    else:
        if string[:len(string) // 2] == string[len(string) // 2:]:
            return True
        else:
            return False


if len(s) <= k:
    a = 2 * ((len(s) + k) // 2)
else:
    a = 2 * k

for i in range(0, len(s) - 1):
    for j in range(i + 1, len(s)):
        if tandem(s[i:j + 1]):
            a = max(a, j - i + 1)

for i in range(len(s) - 1):
    if s[i] == s[-1]:
        x = 0
        while i - x >= 0:
            if s[i - x] == s[-1 - x] and i + x < len(s):
                x += 1
            else:
                break
        if len(s) - i - x - 1 <= k:
            a = max(a, 2 * (len(s) - i - 1))

print(a)
