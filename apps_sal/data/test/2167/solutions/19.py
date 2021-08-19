n = int(input())
a = list(map(int, input().split()))
ans = sum(a)
print(n) if ans % n == 0 else print(n - 1)
