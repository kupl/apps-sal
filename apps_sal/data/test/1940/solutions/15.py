

def ri():
    return list(map(int, input().split()))


n, k = ri()

w = list(ri())

ans = 0
for ww in w:
    if ww % k == 0:
        ans += ww // k
    else:
        ans += ww // k + 1

if ans % 2:
    print(ans // 2 + 1)
else:
    print(ans // 2)

print()
