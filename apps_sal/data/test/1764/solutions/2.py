import itertools
n = int(input())
a = [int(x) for x in input().split()]
winner = a[-1]
looser = 3 - winner
(serve_win_cnt, serve_loose_cnt, win_pos, loose_pos, result) = ([0], [0], [-1], [-1], [])
win_cnt = a.count(winner)
for i in range(n):
    if a[i] == winner:
        win_pos.append(i)
    else:
        loose_pos.append(i)
    serve_win_cnt.append(serve_win_cnt[-1] + (a[i] == winner))
    serve_loose_cnt.append(serve_loose_cnt[-1] + (a[i] == looser))
win_pos += [n * 10] * n
loose_pos += [n * 10] * n
serve_win_cnt += [0] * n
serve_loose_cnt += [0] * n
for t in itertools.chain(list(range(1, 1 + win_cnt // 2)), [win_cnt]):
    s = l = i = 0
    sw = sl = 0
    while i < n:
        xw = win_pos[serve_win_cnt[i] + t]
        xl = loose_pos[serve_loose_cnt[i] + t]
        if xw < xl:
            s += 1
        else:
            l += 1
        i = min(xw, xl) + 1
    if s > l and i <= n and (serve_win_cnt[i] == win_cnt):
        result.append((s, t))
print(len(result))
for (x, y) in sorted(result):
    print(x, y)
