N = input()
f = 0
for num in N:
    f += int(num)
print('Yes' if int(N) % f == 0 else 'No')
