n = int(input())
colors = list(map(int, input().split()))
m = min(colors)
longest_sub = 0
cur_sub = 0
pos = 0
break_on_min = False
while pos < n:
    if colors[pos] > m:
        cur_sub += 1
        if cur_sub > longest_sub:
            longest_sub = cur_sub
    else:
        cur_sub = 0
        if break_on_min:
            break
    pos += 1
    if pos == n and cur_sub > 0:
        pos = 0
        break_on_min = True
print(m * n + longest_sub)
