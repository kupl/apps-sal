from collections import defaultdict


def get_revealed(hid):
    revealed = set()
    for ch in hid:
        if ch != '*':
            revealed.add(ch)
    return revealed


def test_already_shown(s1, s2):
    for i in range(len(s1)):
        if s1[i] != '*' and s1[i] != s2[i]:
            return False
    return True


def check_revealed_present(s1, s2, revealed):
    for i in range(len(s1)):
        if s1[i] == '*':
            if s2[i] in revealed:
                return False
    return True


def process(s1, s2, d):
    temp = set()
    for i in range(len(s1)):
        if s1[i] == '*':
            temp.add(s2[i])
    for i in temp:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d


n = int(input())
hid = input()
revealed = get_revealed(hid)
# print(revealed)
m = int(input())
x = 0
d = {}
for i in range(m):
    s = input()
    if not test_already_shown(hid, s):
        continue
    if not check_revealed_present(hid, s, revealed):
        continue
    d = process(hid, s, d)
    # print("sad")
    x += 1
ans = 0
# print(x,revealed,d)
for i in d:
    if d[i] == x:
        ans += 1
print(ans)
