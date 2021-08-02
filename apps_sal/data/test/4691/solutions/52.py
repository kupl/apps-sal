n = int(input())
a = [0] * 4
b = ["AC", "WA", "TLE", "RE"]
for i in range(n):
    s = input()
    for j in range(4):
        if s == b[j]:
            a[j] += 1
for i in range(4):
    print(b[i] + " x " + str(a[i]))
