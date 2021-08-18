a, b, k = map(int, input().split())
takahashi = [0, a - k]

aoki = [0, b + min(takahashi)]

print("{takahashi} {aoki}".format(takahashi=max(takahashi), aoki=max(aoki)))
