# 初期入力
import sys

# input = sys.stdin.readline  #文字列では使わない
S = input().strip()
T = input().strip()
ans = "No"
for _ in range(len(S)):
    S = S[-1] + S[:-1]
    if S == T:
        ans = "Yes"
print(ans)
