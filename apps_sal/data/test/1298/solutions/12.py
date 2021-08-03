n = int(input())
s = input()
k = 0
for i in s:
    if i == '0':
        k += 1
print(abs(n - 2 * k))
