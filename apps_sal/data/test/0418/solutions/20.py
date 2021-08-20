N = int(input())
ans = 'NO'
for _ in range(N):
    (handle, before, after) = input().split()
    (before, after) = (int(before), int(after))
    if before >= 2400 and after > before:
        ans = 'YES'
print(ans)
