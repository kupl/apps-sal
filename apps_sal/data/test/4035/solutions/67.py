import math
a, b = map(int, input().split())

ma_min, ma_max = math.ceil(a / 0.08), math.ceil((a + 1) / 0.08 - 1)
mb_min, mb_max = math.ceil(b / 0.1), math.ceil((b + 1) / 0.1 - 1)

tmp_ans = max(ma_min, mb_min)
if ma_min <= tmp_ans <= ma_max and mb_min <= tmp_ans <= mb_max:
    ans = tmp_ans
else:
    ans = -1
print(ans)
