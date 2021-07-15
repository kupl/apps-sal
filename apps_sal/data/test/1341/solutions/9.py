s = input()
c = input()
step = 0
for i in range(len(c)):
    if c[i] == s[step]:
        step += 1
print(step+1)

