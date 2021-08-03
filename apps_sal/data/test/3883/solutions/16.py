a, b = list(map(int, input().split()))

if b - a == 0:
    print('%.12f' % (b))

elif int((a - b) / (2 * b)) == 0 and int((a + b) / (2 * b)) == 0:
    print(-1)
else:
    if int((a - b) / (2 * b)) != 0 and int((a + b) / (2 * b)) != 0:
        print('%.12f' % (min(((a - b) / (2 * int((a - b) / (2 * b)))), ((a + b) / (2 * int((a + b) / (2 * b)))))))
    elif int((a - b) / (2 * b)) == 0 and int((a + b) / (2 * b)) != 0:
        print('%.12f' % (((a + b) / (2 * int((a + b) / (2 * b))))))
