n = input()
a = n[0]
b = n[1]
c = n[2]
d = n[3]
e = n[4]
n = a + c + e + d + b
n = int(n)
ans = n ** 5 % 100000
if ans < 10:
    ans = '0000' + str(ans)
elif ans < 100:
    ans = '000' + str(ans)
elif ans < 1000:
    ans = '00' + str(ans)
elif ans < 10000:
    ans = '0' + str(ans)
print(ans)
