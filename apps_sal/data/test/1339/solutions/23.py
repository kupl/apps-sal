n = int(input())
(minn, maxn) = (int(i) for i in input().split())
numbers = {(minn, maxn): 0}
for j in range(1, n):
    (a, b) = (int(i) for i in input().split())
    numbers[a, b] = j
    if b > maxn:
        maxn = b
    if a < minn:
        minn = a
if (minn, maxn) in numbers:
    print(numbers[minn, maxn] + 1)
else:
    print(-1)
