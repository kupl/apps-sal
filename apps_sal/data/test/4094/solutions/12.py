k = int(input())

num = 7 % k
ans = 1
mod = [0 for _ in range(k)]
mod[num] = 1
while(num):
    num = (num * 10 + 7) % k
    if mod[num] > 0:
        ans = -1
        break
    ans += 1
    mod[num] += 1

print(ans)
