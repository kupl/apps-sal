from collections import defaultdict as dd
from math import factorial as f

s = input()

cnt = dd(int)

for i in s:
    cnt[i] += 1

ans = 0


def calc(cur_chr, dem, do_not_take_sum, total, diff):
    nonlocal ans
    nonlocal cnt

    if cur_chr == '9':
        for do_not_take in range(0, cnt[cur_chr] + 1):
            if do_not_take > 0 and do_not_take == cnt[cur_chr]:
                continue

            cur_do_not_take_sum = do_not_take_sum + do_not_take
            if cur_do_not_take_sum == total:
                continue

            cur_dem = dem * f(cnt[cur_chr] - do_not_take)
            num = f(total - cur_do_not_take_sum)

            ans += num // cur_dem * diff
        return

    for do_not_take in range(0, cnt[cur_chr] + 1):
        if do_not_take > 0 and do_not_take == cnt[cur_chr]:
            if not(diff == -1 and cur_chr == '0'):
                continue
        calc(chr(ord(cur_chr) + 1), dem * f(cnt[cur_chr] - do_not_take), do_not_take_sum + do_not_take, total, diff)


calc('0', 1, 0, len(s), 1)

if cnt['0'] != 0:
    cnt['0'] -= 1
    calc('0', 1, 0, len(s) - 1, -1)

print(ans)
