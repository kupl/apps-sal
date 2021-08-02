n = int(input())
a = input()
for i in range(n - 1):
    if (ord(a[i]) > ord(a[i + 1])):
        print(a[:i] + a[i + 1:])
        return
print(a[:n - 1])
