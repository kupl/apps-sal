w, l = list(map(int, input().split()))
a = list(map(int, input().split()))

minsegment = s = sum(a[:l])

for i in range(1, w - l):
    s = s - a[i - 1] + a[i + l - 1]
    minsegment = min(s, minsegment)

print(minsegment)
