a = [chr(i) for i in range(ord('a'), ord('z') + 1)]
s = input()
min_dom = len(s)
for letter in a:
    if letter in s:
        cur = s.index(letter) + 1
        last = cur - 1
        ll = cur - 1
        for j in range(ll + 1, len(s)):
            if s[j] == letter:
                cur = max(cur, j - last)
                last = j
        min_dom = min(min_dom, max(cur, len(s) - last))
print(min_dom)
