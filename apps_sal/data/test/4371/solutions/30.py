n = input()
count = 1000
for i in range(len(n) - 2):
    count = min(count, abs(753 - int(n[i:i + 3])))
print(count)
