N, K = map(int, input().split())
S = str(input())


def run_length_encoding(text: str) -> list:
    text += '_'
    c = text[0]
    x = 1
    res = []
    for i in range(1, len(text)):
        if c == text[i]:
            x += 1
        else:
            res.append((c, x))
            c = text[i]
            x = 1
    return res


rle = run_length_encoding(S)
gr = len(rle)
hp = 0
for c, x in rle:
    hp += x - 1

if gr == 1:
    ans = hp
elif gr == 2:
    ans = hp + 1
else:
    if K < gr // 2:
        ans = hp + 2 * K
    else:
        ans = hp + 2 * ((gr - 1) // 2) + (gr - 1) % 2
print(ans)
