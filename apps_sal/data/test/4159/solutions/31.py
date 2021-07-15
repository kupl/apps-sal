a, b, k = map(int, input().split())
# A - Kを求める
takahashi = [0, a-k] 

# A - K < 0 なら Bの分も食べる
aoki = [0, b + min(takahashi)]

print("{takahashi} {aoki}".format(takahashi = max(takahashi), aoki = max(aoki)))
