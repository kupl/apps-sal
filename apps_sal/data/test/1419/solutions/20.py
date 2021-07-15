# The first line contains number k (1 ≤ k ≤ 105).

# The second line contains the text of the ad —
# non-empty space-separated words of lowercase and uppercase Latin letters and hyphens.

K = int(input())

line = input()
line = line.replace('-', ' ')
text = line.split()
ords = list(map(len, text))
words = [x+1 for x in ords]
words[-1] -= 1

def can(limit):
    row = 0
    col = 0
    win = 0
    while win < len(words):
        while (win < len(words) and col + words[win] <= limit):
            col += words[win]
            # print(text[win], end = '.')
            win += 1
        row += 1
        # print()
        col = 0
    return row < K or (row <= K and col == 0)

lo = max(words)

hi = len(line)

while lo < hi:
    mid = (lo + hi) // 2
    # print(f'mid={mid}')
    # mid = lo + (hi - lo) // 2
    if can(mid):
        hi = mid
    else:
        lo = mid + 1

print(hi)

