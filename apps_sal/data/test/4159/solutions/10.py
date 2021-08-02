a, b, k = map(int, input().split())
# A - Kを求める
remain = a - k
takahashi = remain
# A - K < 0 なら Bの分も食べる
aoki = b
if remain < 0:
    takahashi = 0
    aoki = b + remain

print(str(takahashi) + " " + str(aoki if aoki > 0 else 0))
