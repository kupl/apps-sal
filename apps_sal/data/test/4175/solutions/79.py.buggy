n = int(input())
li = [input() for i in range(n)]

for i in range(n - 1):
    for j in range(i + 1, n):
        if li[i] == li[j]:
            print('No')
            return

for i in range(n - 1):
    if li[i][-1] != li[i + 1][0]:
        print('No')
        return
print('Yes')
