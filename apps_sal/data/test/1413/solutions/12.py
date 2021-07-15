n = int(input())
s = input()
num = 0
for i in range(n):
    if int(s[i]) % 2 == 0:
        num += i+1
print(num)

