fax = input()
i = int(input())

if len(fax) % i != 0:
    print('NO')
else:
    for m in range(i):
        temp = fax[m * (len(fax) // i): (m + 1) * (len(fax) // i)]
        if temp != temp[::-1]:
            print('NO')
            break
    else:
        print('YES')

