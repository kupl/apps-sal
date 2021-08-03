a = list(input())
num = len(a)
count = 0
for i in range(len(a) // 2):
    if a[i] == a[num - 1 - i]:
        pass
    else:
        count += 1
print(count)
