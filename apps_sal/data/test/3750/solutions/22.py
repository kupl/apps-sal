k, a, b = [int(x) for x in input().split()]
ans = a // k + b // k
if ans == 0 or (a % k != 0 and b < k) or (b % k != 0 and a < k):
    ans = -1
print(ans)
