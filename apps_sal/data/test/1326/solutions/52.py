N = int(input())
ans = 0
for i in range(1, N + 1):
    tmp = N // i
    ans += ((tmp * i + i) * tmp) / 2
print(int(ans))
