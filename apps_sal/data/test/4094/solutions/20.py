K = int(input())
mod = 7 % K
ans = -1

for k in range(K):
    if mod == 0:
        ans = k + 1
        break
    mod = (mod * 10 + 7) % K

print(ans)
