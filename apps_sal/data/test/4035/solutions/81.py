a, b = map(int, input().split())
i = 1
f = 0
while True:
    if int(i*0.08)==a and int(i*0.1)==b:
        print(i)
        f = 1
        break
    if int(i*0.08)>a:
        break
    i += 1
if not f:
    print(-1)
