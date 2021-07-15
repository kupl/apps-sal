n = int(input())
a = list(map(int, input().split()))
print("YES" if (n == 1 and a.count(0) == 0) or (n > 1 and a.count(0) == 1) else "NO")
