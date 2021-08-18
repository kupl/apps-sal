n = int(input())
L = list(map(int, input().split()))
if (n > 1 and sum(L) == n - 1) or (n == 1 and sum(L) == n):
    print("YES")
else:
    print("NO")
