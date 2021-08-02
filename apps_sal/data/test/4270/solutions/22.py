n = int(input())
v = list(map(int, input().split()))
v_s = sorted(v)
m = v_s[0]
for i in range(n - 1):
    m = (m + v_s[i + 1]) / 2
print(m)
