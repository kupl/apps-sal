(n, m) = list(map(int, input().split()))
num = [int(x) for x in input().split()]
Min = Sum = Pos = 0
for i in range(m):
    Sum += num[i]
Min = Sum
for i in range(m, n):
    Sum += num[i] - num[i - m]
    if Min > Sum:
        Min = Sum
        Pos = i - m + 1
print(Pos + 1)
