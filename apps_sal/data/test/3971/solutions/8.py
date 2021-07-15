n = int(input())
t = list(map(int, input().split()))
s = [0] * 100001
for i in t: s[i] += 1
a = b = 0
for i in range(100001): a, b = max(a, b), a + s[i] * i
print(max(a, b))
