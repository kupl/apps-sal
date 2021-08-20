(m, k) = list(map(int, input().split()))
d = list(map(int, input().split()))
s = list(map(int, input().split()))
cap = 0
dis = 0
ma = 0
time = 0
for i in range(m):
    dis = d[i]
    cap += s[i] - d[i]
    time += d[i]
    ma = max(ma, s[i])
    if cap < 0:
        while cap < 0:
            cap += ma
            time += k
print(time)
