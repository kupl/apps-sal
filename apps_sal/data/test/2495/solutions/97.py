N = int(input())
A = [int(i) for i in input().split()]
ans = 0
s = 0
for i in range(N):
    s += A[i]
    if i % 2 == 0:
        if s <= 0:
            ans += 1 - s
            s = 1
    elif s >= 0:
        ans += s + 1
        s = -1
nums = 0
s = 0
for i in range(N):
    s += A[i]
    if i % 2 != 0:
        if s <= 0:
            nums += 1 - s
            s = 1
    elif s >= 0:
        nums += s + 1
        s = -1
print(min(nums, ans))
