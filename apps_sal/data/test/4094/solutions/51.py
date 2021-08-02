k = int(input())
ans = -1
mod = 7 % k

for i in range(k):
    if mod == 0:
        ans = i + 1
        break
    mod = (mod * 10 + 7) % k
print(ans)
