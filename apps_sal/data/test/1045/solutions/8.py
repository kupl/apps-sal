n = int(input())
s = i = level = 0
while 1:
    i += 1
    level += i
    s += level
    if s > n:
        i -= 1
        break
print(i)
