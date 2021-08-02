n = int(input())
s = [i for i in range(1, n + 1)]
counter = 0
while(True):
    if len(s) == 1:
        print((1))
        break
    if len([i for i in s if i % 2 == 0]) == 1:
        s = [i for i in s if i % 2 == 0]
        print((int(s[0]) * (2 ** counter)))
        break
    else:
        s = [i / 2 for i in s]
        counter += 1
