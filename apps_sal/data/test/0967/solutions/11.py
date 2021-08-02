n = int(input())
a = (str(input())).split(' ')
ma = 0
output = 0
for i in range(n - 1):
    if int(a[i]) < int(a[i + 1]):
        ma += 1
    else:
        output += 1 + ma
        ma = 0
print(output)
