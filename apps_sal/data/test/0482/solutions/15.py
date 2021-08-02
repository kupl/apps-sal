nk = input().split()
n = int(nk[0])
k = int(nk[1])
password = ''
i = 0
j = 0
for i in range(n):
    if j < k:
        password = password + chr(97 + j)
        j += 1
    else:
        j = 0
        password = password + chr(97 + j)
        j += 1
print(password)
