n = int(input())
l = list(map(int, input().strip().split(' ')))
p = 1
l.sort()
length = len(l)
ans = 0
for i in range(len(l)):
    ans += p * (l[i] - l[length - i - 1])
    p *= 2
    p %= 1000000007
    ans %= 1000000007

print(int(ans))
