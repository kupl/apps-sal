(n, x) = map(int, input().split())
A = set(map(int, input().split()))
cnt = (x in A) + sum((i not in A for i in range(x)))
print(cnt)
