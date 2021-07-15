N = int(input())
A = list(map(int, input().split()))

ans = 0

for a in A:
    ans_ = 0
    while a % 2 == 0:
        a //= 2
        ans_ += 1
    ans += ans_

print(ans)
