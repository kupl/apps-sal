n = input()
p = '-1'
s = 0
for i in range(0, len(n) - 1):
    if int(n[i]) % 2 == 0 and int(n[i]) < int(n[len(n) - 1]):
        k = n[i]
        s = 1
        p = n[0:i] + n[len(n) - 1] + n[i + 1:len(n) - 1] + k
        break
if s != 1:
    for i in range(len(n) - 1, -1, -1):
        if int(n[i]) % 2 == 0:
            k = n[i]
            p = n[0:i] + n[len(n) - 1] + n[i + 1:len(n) - 1] + k
            break
print(p)
