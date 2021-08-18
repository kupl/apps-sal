n, k = list(map(int, input().split()))
xlst = list(map(int, input().split()))
minus = []
plus = []
for x in xlst:
    if x < 0:
        minus.append(-1 * x)
    elif x > 0:
        plus.append(x)
    else:
        k -= 1
if k == 0:
    print((0))
    return
minus.append(0)
minus = minus[::-1]
plus = [0] + plus
ans = 10 ** 20
ml = len(minus)
pl = len(plus)

pos = min(k, ml - 1)
while 1:
    mm = minus[pos]
    pp = plus[k - pos]
    ans_tmp = max(mm, pp) + min(mm, pp) * 2
    ans = min(ans, ans_tmp)
    pos -= 1
    if pos == -1 or k - pos == pl:
        break
print(ans)
