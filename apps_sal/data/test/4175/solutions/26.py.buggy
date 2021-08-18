n = int(input())
a = []
c = 0
for _ in range(n):
    w = input()
    a.append(w)

for i in range(1, n):
    if a[i - 1][-1] != a[i][0]:
        print('No')
        return
if n != len(set(a)):
    print('No')
    return
print('Yes')
