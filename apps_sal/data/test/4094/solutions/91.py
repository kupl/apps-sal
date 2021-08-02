#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

k = int(input())

t = 7
for i in range(k):
    t = t % k
    if t == 0:
        print((i + 1))
        return
    else:
        t = t * 10 + 7
print((-1))
