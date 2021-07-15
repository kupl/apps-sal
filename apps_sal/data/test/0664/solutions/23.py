n = int(input())
t = list(map(int, input().split()))
i = 1
while i < n and t[i] >= t[i - 1]: i += 1
if i == n: print(0)
else:
    j = i + 1
    while j < n and t[j] >= t[j - 1]: j += 1
    print(-1 if j < n or t[0] < t[-1] else n - i)
