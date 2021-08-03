minday = maxday = 0

for i in range(int(input())):
    k = i % 7
    if k == 0 or k == 1:
        maxday += 1
    if k == 5 or k == 6:
        minday += 1

print(minday, maxday)
