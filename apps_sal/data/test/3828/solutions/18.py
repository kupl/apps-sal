n = int(input())
m = [0] * (n + 1)
l = list(map(int, input().split()))
for i in l:
    m[i] = m[i - 1] + 1
print(n - max(m))
