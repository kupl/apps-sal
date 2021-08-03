n = input()
a = list(map(int, input().split()))
sum = 0
msum = 0
for i in a:
    sum += i
    msum += i * i
ans = int((sum * sum - msum) // 2)
print(int(ans % 1000000007))
