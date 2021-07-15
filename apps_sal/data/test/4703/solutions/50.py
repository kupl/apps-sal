# 毎回挿れるか挿れないかの二択の探索をしてみる
# 2値なのでbit全探索をやってみる
# 逆ポーランド必要か？と思ったけど加算だけだしいらんかったわ助かる
s = input()
ans = 0
for bit in range(0, 1 << len(s) - 1):
    opr = []
    for i in range(len(s) - 1):
        opr.append("水着" if bit >> i & 1 == 1 else "ワンピース")
    exp = [s[0]]
    for i in range(len(opr)):
        if opr[i] == "ワンピース":
            exp[-1] += s[i + 1]
        elif opr[i] == "水着":
            exp.append(s[i + 1])
    ans += sum(list(map(int, exp)))
print(ans)

