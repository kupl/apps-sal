def avv(l, s, n):
    i = 0
    while i < n:
        ss = l[i] + l[n]
        if ss > s:
            n -= 1
        elif ss < s:
            i += 1
        else:
            return True
    return False


l = []
for _ in range(int(input())):
    l.append(int(input()))
avg = 0; l.sort()
for i in range(len(l)):
    if avv(l, 2 * l[i], len(l) - 1):
        avg += 1
print(avg)
