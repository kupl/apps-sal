(a, b) = map(int, input().split())
count = 0
for i in range(a, b + 1):
    if str(i)[0] == str(i)[4] and str(i)[1] == str(i)[3]:
        count += 1
print(count)
