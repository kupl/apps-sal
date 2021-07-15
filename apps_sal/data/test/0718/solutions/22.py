a = int(input())
c = 0
for i in range(a + 1,  8888888889):
    c += 1
    if '8' in str(i):
        print(c)
        break
