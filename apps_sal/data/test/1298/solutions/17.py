import string
n = input()
s = str(input())
z_count = 0
o_count = 0
for i in s:
    if i == '1':
        o_count += 1
    if i == '0':
        z_count += 1
ans = abs(o_count - z_count)
print(ans)
