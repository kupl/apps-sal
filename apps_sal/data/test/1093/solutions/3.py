h, w = list(map(int, input().split()))
high = [0 for i in range(w)]
for i in range(h, 0, -1):
    s = input()
    for j in range(w):
        if s[j] == '*':
            high[j] = max(i, high[j])
mx = 0
mn = 0
for i in range(w - 1):
    mx = max(mx, high[i + 1] - high[i])
    mn = min(mn, high[i + 1] - high[i])
print(abs(mx), abs(mn))
