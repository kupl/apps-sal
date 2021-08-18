n = int(input())
a = list(input())

f = ['0']
f.extend(list(input().split()))

started = False
for i, item in enumerate(a):
    if not started:
        if int(f[int(item)]) > int(item):
            a[i] = f[int(item)]
            started = True
    else:
        if int(f[int(item)]) >= int(item):
            a[i] = f[int(item)]
        else:
            break

print(''.join(a))
