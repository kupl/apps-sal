n = int(input())
s = input()
slime_end = '0'
num = 0
for i in range(n):
    if s[i] != slime_end:
        num += 1
        slime_end = s[i]
print(num)
