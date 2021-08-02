a = list(input().lower())
b = int(input())
for i in range(len(a)):
    if ord(a[i]) - ord('a') < b:
        a[i] = a[i].upper()
print(''.join(a))
