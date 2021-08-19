# 問題:文字の先頭が'i'で末尾が'j', 且つ文字の先頭が'j'で末尾が'i'のペアはいくつ？
# 'n'以下の全ての数について 先頭を'i', 末尾が'j'としたDBを作成

n = int(input())
# cnt[i][j] := 先頭が'i', 末尾が'j'の数
cnt = [[0] * 10 for _ in range(10)]

for i in range(1, n + 1):
    cnt[int(str(i)[0])][int(str(i)[-1])] += 1

# 先頭が'i'で末尾が'j'の総数 [掛ける] 先頭が'j'で末尾が'i'の総数の総和が'ans'
ans = 0
for i in range(10):
    for j in range(10):
        ans += cnt[i][j] * cnt[j][i]

print(ans)
