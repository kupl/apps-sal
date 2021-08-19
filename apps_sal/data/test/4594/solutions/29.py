N = int(input())
d = []
for _ in range(N):
    d.append(int(input()))
d.sort(reverse=True)
top = 101
ans = 0
for d_ in d:
    if d_ < top:
        ans += 1
        top = d_
print(ans)
