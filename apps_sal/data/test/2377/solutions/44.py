# Bを一回使えると考えると
# - Ai>BiであるBiを使う意味はない(Aiで殴ればいいので)
# - Ai>AjであるAjを使う意味はない（Aiで殴ればいいので）
# つまりA中最強のAiより上（i=j自身を含む）のBjを1度使い、あとはAiで殴る
n, h = map(int, input().split())
power = [list(map(int, input().split())) for _ in range(n)]
maxa = sorted(power, key=lambda x: x[0], reverse=True)[0][0]
muscleb = sorted(list(filter(lambda x: x[1] >= maxa, power)), key=lambda x: x[1], reverse=True)
ans = 0
for m in muscleb:
    ans += 1
    h -= m[1]
    if h <= 0:
        print(ans)
        return
additionala = h // maxa
if h % maxa != 0:
    additionala += 1
print(additionala + ans)
