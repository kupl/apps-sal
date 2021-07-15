n = int(input())
lst = list(map(int, input().split()))
tall = lst[0]
ans = 0
for i in range(1, n):
    if tall > lst[i]:
        ans += tall - lst[i]
    else:
        tall = lst[i]
print(ans)

