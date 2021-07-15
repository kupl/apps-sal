mod = 1000000000+7

n = int(input())
As = list(map(int, input().split()))


sum_ = sum(As)
ret = 0
for i in range(n-1):
    sum_ -= As[n-1-i]
    ret += sum_ * As[n-1-i]
    ret %= mod

print(ret)
