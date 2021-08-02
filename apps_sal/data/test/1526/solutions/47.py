l = list(map(int, input().split()))
ref = max(l) * 3 - sum(l)

if ref % 2 == 0:
    ans = ref // 2
else:
    ans = ref // 2 + 2

print(ans)
