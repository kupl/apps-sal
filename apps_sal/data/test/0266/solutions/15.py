__author__ = 'user'
(m, s) = map(int, input().split())
if s == 0 and m > 1 or s > 9 * m:
    min_num = max_num = -1
elif m == 1:
    min_num = max_num = s
else:
    nns1 = s // 9
    d = s % 9
    max_num = '9' * nns1
    if nns1 != m:
        max_num += str(d) + '0' * (m - nns1 - 1)
    if s <= (m - 1) * 9:
        nns2 = (s - 1) // 9
        d = (s - 1) % 9
        min_num = '1' + '0' * (m - nns2 - 1 - 1)
        if nns2 != m:
            min_num += str(d) + '9' * nns2
    else:
        min_num = ''
        if s // 9 != m:
            min_num = str(s % 9)
        min_num += '9' * (s // 9)
print(min_num, max_num)
