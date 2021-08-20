a = input().split()
b = int(''.join(a))
num = int(100100 ** 1 / 2)
ans = 'No'
for i in range(num):
    if i ** 2 == b:
        ans = 'Yes'
        break
print(ans)
