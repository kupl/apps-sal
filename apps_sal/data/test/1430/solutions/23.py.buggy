def rle(string):
    _rle_str = string[0]
    _rle_cnt = 1
    _ans_l = []
    for _i in range(1, len(string)):
        if _rle_str == string[_i]:
            _rle_cnt += 1
        else:
            _ans_l.append([_rle_str, _rle_cnt])
            _rle_str = string[_i]
            _rle_cnt = 1
    _ans_l.append([_rle_str, _rle_cnt])
    return _ans_l


n, k = list(map(int, input().split()))
s = input()

rs = rle(s)

if rs[0][0] == "0":
    cnt = 1
    wa = rs[0][1]
    r = 1
    l = 0
else:
    cnt = 0
    wa = 0
    r = 0
    l = 0

ans = -1

if len(rs) == 1:
    print((rs[0][1]))
    return

while r < len(rs):
    if cnt == k and rs[r][0] == "0":
        if rs[l][0] == "0":
            wa -= rs[l][1]
            cnt -= 1
        else:
            wa -= rs[l][1]
        l += 1

    elif cnt <= k:
        if rs[r][0] == "0":
            cnt += 1
            wa += rs[r][1]
        else:
            wa += rs[r][1]
        r += 1
        ans = max(ans, wa)

    else:
        if rs[l][0] == "0":
            wa -= rs[l][1]
            cnt -= 1
        else:
            wa -= rs[l][1]
        l += 1

print(ans)
