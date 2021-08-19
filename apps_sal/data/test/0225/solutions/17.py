(a, b, c, d) = map(lambda x: int(x), input().split())
step1 = [0]
step2 = []
step3 = []
step4 = []
step5 = []
for x in step1:
    step2.append(x + a)
    step2.append(x - a)
for x in step2:
    step3.append(x + b)
    step3.append(x - b)
for x in step3:
    step4.append(x + c)
    step4.append(x - c)
for x in step4:
    step5.append(x + d)
    step5.append(x - d)
print('YES' if 0 in step5 else 'NO')
