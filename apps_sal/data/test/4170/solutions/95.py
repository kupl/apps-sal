N = int(input())
H = list(map(int, input().split()))
ans = 0
p = 0
for i in range(N - 1):
    if H[i] < H[i + 1]:
        if ans < p:
            ans = p
        p = 0
    else:
        p += 1
if ans < p:
    ans = p
print(ans)
