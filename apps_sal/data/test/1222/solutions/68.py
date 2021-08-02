k = int(input())

a = [str(i) for i in range(1, 10)]

cnt = 9

if k <= 9:
    print(k)
    return
else:
    while True:
        b = a.pop(0)
        c = int(b) % 10
        d = c + 1
        e = c - 1
        if b[-1] == '0':
            a.append(str(b) + str(c))
            a.append(str(b) + str(d))
            cnt += 2
        elif b[-1] == '9':
            a.append(str(b) + str(e))
            a.append(str(b) + str(c))
            cnt += 2
        else:
            a.append(str(b) + str(e))
            a.append(str(b) + str(c))
            a.append(str(b) + str(d))
            cnt += 3
        if cnt >= k:
            break
print((a[-(cnt - k + 1)]))
# print(a)
