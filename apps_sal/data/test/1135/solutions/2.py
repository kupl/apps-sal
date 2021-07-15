n = int(input())
s = input()

if n % 2 == 1:
    res = s[n - 2:0:-2] + s[0] + s[2::2]
else:
    res = s[n - 2::-2] + s[1::2]

print(res)
