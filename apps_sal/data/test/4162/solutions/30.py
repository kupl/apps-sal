# モジュールのインポート
import fractions

# 標準入力を取得
N = int(input())
a = list(map(int, input().split()))

# 求解処理
ans = sum(a) - N

# 結果出力
print(ans)
