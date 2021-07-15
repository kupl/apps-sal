from sys import stdin, stdout
n = int(stdin.readline())
colours = stdin.readline().strip()
cntf, cnts = 0, 0

label = colours[0]

for i in range(n):
    if i % 2 and label == colours[i]:
        cntf += 1
    elif not i % 2 and label != colours[i]:
        cnts += 1
ans = max(cntf, cnts)

cntf, cnts = 0, 0
for i in range(n):
    if i % 2 and label != colours[i]:
        cntf += 1
    elif not i % 2 and label == colours[i]:
        cnts += 1
ans = min(ans, max(cntf, cnts))


stdout.write(str(ans))   
