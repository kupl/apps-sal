n = int(input())
a = list(map(int, input().split()))
min_en = 10000000000
for i in range(n):
    x = i
    en = 0
    for j in range(n):
        en += (abs(j - x) + abs(j) + abs(x)) * 2 * a[j]
    if en < min_en:
        min_en = en
print(min_en)
