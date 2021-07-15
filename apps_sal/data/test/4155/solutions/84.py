n = int(input())
h = list(map(int, input().split()))

ans = 0
active = 0

for i in range(n):
    if active >= h[i]:
        active = h[i]
        #区間の最小値を左端に更新
    else:
        ans += h[i] - active
        #見てきた値と現在値（最大）との差を求める
        active = h[i]
        #activeを現在の値に更新

print(ans)
