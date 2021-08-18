
red_cards = []
blue_cards = []
N = int(input())
for i in range(N):
    blue_cards.append(input())
M = int(input())
for i in range(M):
    red_cards.append(input())


all_words = set(blue_cards + red_cards)

ans = 0
for i, w in enumerate(all_words):
    cnt_b = cnt_r = 0
    for b in blue_cards:
        if b == w:
            cnt_b += 1
    for r in red_cards:
        if r == w:
            cnt_r += 1

    diff = cnt_b - cnt_r
    if diff > ans:
        ans = diff

print(ans)
