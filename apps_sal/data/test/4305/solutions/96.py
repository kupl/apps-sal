H, A = map(int, input().split())
ans = H // A
mod = H % A
if mod == 0:
    print(ans)
else:
    print(ans + 1)
