a, b, k = map(int, input().split())
remain = a - k
takahashi = remain
aoki = b
if remain < 0:
    takahashi = 0
    aoki = b + remain

print(str(takahashi) + " " + str(aoki if aoki > 0 else 0))
