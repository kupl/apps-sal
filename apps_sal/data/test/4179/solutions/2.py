ans = 0
n, m, c = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n):
    a = list(map(int, input().split()))
    tmp = sum([a_ * b_ for (a_, b_) in zip(a, b)]) + c
    if tmp > 0:
        ans += 1

print(ans)
