a = list(map(int, input().split()))

s = sum(a)

for i in range(6):
    for j in range(6):
        for k in range(6):
            if i == j or j == k or i == k:
                pass
            else:
                ts = a[i] + a[j] + a[k]
                if ts == s - ts:
                    print("YES")
                    return

print("NO")
