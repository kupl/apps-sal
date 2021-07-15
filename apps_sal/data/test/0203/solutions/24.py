n = input()
a = input()
cnt = 0
while len(set(a)) == 2:
    new_a = []
    for i in range(len(a)):
        if a[i] == 'D':
            if cnt >= 0:
                new_a.append(a[i])
            cnt += 1
        else:
            if cnt <= 0:
                new_a.append(a[i])
            cnt -= 1
    a = new_a
print(a[0])


