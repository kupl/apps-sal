n, m = [int(x) for x in input().split()]
a = [y for y in reversed([int(x) for x in input().split()])]
t = 0
cur_pos = 1
while len(a) > 0:
    nxt = a.pop()
    if nxt > cur_pos:
        t += nxt - cur_pos
    elif nxt < cur_pos:
        t += n - (cur_pos - nxt)
    cur_pos = nxt

print(t)
