(n, m, r) = map(int, input().split())
buys = list(map(int, input().split()))
sells = list(map(int, input().split()))
min_buys = min(buys)
max_selss = max(sells)
if min_buys < max_selss:
    print(r % min_buys + r // min_buys * max_selss)
else:
    print(r)
