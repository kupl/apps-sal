X = int(input())
count = 0
saving = 100
while saving < X:
    saving += saving // 100
    count += 1
print(count)
