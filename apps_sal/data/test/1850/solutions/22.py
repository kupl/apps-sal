n, d = map(int, input().split())
s = list(map(int, input().split()))
k = list(map(int, input().split()))
x = s[d - 1] + k[0]
j = 0
o = 0
for i in range(d - 2, -1, -1):
    j += 1
    while j < len(k) and s[i] + k[j] > x:
        j += 1
    if j >= len(k):
        o = i + 1
        break
print(o + 1)
