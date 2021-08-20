import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
ans1 = sum(a[0:(n + 1) // 2])
ans2 = sum(a[(n + 1) // 2:n])
print(ans1 ** 2 + ans2 ** 2)
