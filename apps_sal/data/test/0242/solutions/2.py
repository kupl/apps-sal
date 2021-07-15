a = int(input())
i = 0
cnt = 0
while cnt < a:
    i += 5
    i1 = i
    while i1 % 5 == 0:
        i1 //= 5
        cnt += 1
if cnt == a:
    print(5)
    for s in range(i, i+5):
        print(s, end=' ')
else:
    print(0)
