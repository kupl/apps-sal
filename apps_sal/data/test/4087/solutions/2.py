def check(a):
    s = str(a)
    t = 0
    for el in s:
        t += int(el)
    return t % 4 == 0


n = int(input())
while not check(n):
    n += 1
print(n)
