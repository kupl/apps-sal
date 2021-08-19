N = input()
n = len(N)
total = 0
for i in range(n):
    total += int(N[i])
if total % 9 == 0:
    print('Yes')
else:
    print('No')
