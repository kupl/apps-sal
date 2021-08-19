(N, T, C) = map(int, input().split())
pics = [-1]
for (index, s) in enumerate(map(int, input().split())):
    if s > T:
        pics.append(index)
pics.append(N)
ans = 0
for (picIndex, pic) in enumerate(pics):
    diff = pic - pics[picIndex - 1] - 1
    ans += max(diff - C + 1, 0)
print(ans)
