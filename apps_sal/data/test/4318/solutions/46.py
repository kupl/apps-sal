n = int(input())
hi = list(map(int, input().split()))
ans = [hi[0]]
hi0 = hi[0]
for i in hi[1:]:
    if hi0 <= i:
        ans.append(i)
        hi0 = max(hi0, i)

print(len(ans))
