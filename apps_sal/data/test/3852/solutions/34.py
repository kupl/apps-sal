n = int(input())
A = list(int(x) for x in input().split())
minimum = min(A)
maximum = max(A)

ANS = []
if abs(maximum) >= abs(minimum):  # すべてをプラスにして累積和
    index = A.index(maximum)
    for i in range(n):
        ANS.append((index, i))
        # A[i] += maximum
    for i in range(n - 1):
        ANS.append((i, i + 1))
        # A[i+1] += A[i]
else:  # 最小値がマイナスで絶対値がかなり大きい -> n回ですべてをマイナスにして累積和
    index = A.index(minimum)
    for i in range(n):
        ANS.append((index, i))
        # A[i] += minimum
    for i in reversed(list(range(1, n))):
        ANS.append((i, i - 1))
        # A[i-1] += A[i]

print((len(ANS)))
for x, y in ANS:
    print((x + 1, y + 1))  # 1-index

# print(A)

