n = int(input())
a = input()
for i in range(1, n):
    if a[i] == a[i - 1] and a[i] != '?':
        print('No')
        return

for i in range(n):
    if a[i] == '?':
        if i == 0 or i == n - 1:
            print('Yes')
            return
        elif a[i - 1] == '?' or a[i + 1] == '?':
            print('Yes')
            return
        else:
            if a[i - 1] == a[i + 1]:
                print('Yes')
                return
print('No')
