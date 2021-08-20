n = int(input())
a_list = list(map(int, list(str(input()).split(' '))))
out = [' ' * sum(a_list)] * 2000
(cur, pref_size) = (1000, 0)
(cur_max, cur_min) = (1000, 1000)
for k in range(n):
    for i in range(a_list[k]):
        ind = pref_size + i
        if k % 2 == 0:
            out[cur] = out[cur][:ind] + '/' + out[cur][ind + 1:]
            cur += 1
        else:
            out[cur] = out[cur][:ind] + '\\' + out[cur][ind + 1:]
            cur -= 1
    if k % 2 == 1:
        cur += 1
        cur_min = min(cur_min, cur)
    else:
        cur -= 1
        cur_max = max(cur_max, cur)
    pref_size += a_list[k]
for i in range(cur_max, cur_min - 1, -1):
    print(out[i])
