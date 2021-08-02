N = int(input())
A = [int(i) for i in input().split()]
ans = 0
# i%2が正
s = 0
for i in range(N):
    s += A[i]
    if i % 2 == 0:
        if s <= 0:
            ans += 1 - s
            s = 1
    else:
        if s >= 0:
            ans += s + 1
            s = -1
    # print(s,ans)
nums = 0
s = 0
for i in range(N):
    s += A[i]
    if i % 2 != 0:
        if s <= 0:
            nums += 1 - s
            s = 1
    else:
        if s >= 0:
            nums += s + 1
            s = -1
    # print(s,nums)
print(min(nums, ans))
