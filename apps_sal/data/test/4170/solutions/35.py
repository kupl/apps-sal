N = int(input())
H = list(map(int, input().split()))
ans = [0]
for (h1, h2) in zip(H, H[1:]):
    if h2 <= h1:
        ans += [ans[-1] + 1]
    else:
        ans += [0]
print(max(ans))
