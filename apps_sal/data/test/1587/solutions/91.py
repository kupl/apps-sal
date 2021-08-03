n = int(input())
c = input()

# それぞれの色の数をカウント
w = c.count("W")
r = c.count("R")

ans = 0
for i in range(r):  # 　赤の数分文字列を確認する
    if c[i] == "W":
        ans += 1  # カウント
print(ans)
