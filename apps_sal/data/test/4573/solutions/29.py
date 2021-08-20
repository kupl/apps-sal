n = int(input())
X = list(map(int, input().split()))
s = sorted(X)
med_low = s[n // 2 - 1]
med_high = s[n // 2]
for x in X:
    if x <= med_low:
        print(med_high)
    else:
        print(med_low)
