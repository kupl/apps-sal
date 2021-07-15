n = int(input())
s = sum(map(int, input().split()))
if (s == n - 1 and n > 1) or (s == 1 and n == 1):
    print("YES")
else:
    print("NO")
