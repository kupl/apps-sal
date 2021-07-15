n = int(input())
t = list(map(int, input().split()))
s, k = 0, sum(t) // n
t = [i - k for i in t]
for i in range(n - 1):
    s += abs(t[i])
    t[i + 1] += t[i]
print(s)
