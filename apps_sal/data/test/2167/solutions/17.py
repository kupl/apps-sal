n = int(input())
ss = sum(map(int, input().split()))
print(n if ss % n == 0 else n - 1)
