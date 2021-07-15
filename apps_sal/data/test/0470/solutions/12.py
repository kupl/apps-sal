a = list(map(int, input().split()))
b = [0]*150
ma = 0
for i in range(5):
    b[a[i]] += 1
    if b[a[i]] > 1:
        if b[a[i]]*a[i] > ma and b[a[i]] < 4:
            ma = b[a[i]]*a[i]
print(sum(a) - ma)
