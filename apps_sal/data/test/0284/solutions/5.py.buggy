n = int(input())

for i in range(n // 1234567 + 1):
    ii = n - i * 1234567
    if ii == 0:
        print("YES")
        return
    for j in range(ii // 123456 + 1):
        jj = ii - j * 123456
        if jj == 0:
            print("YES")
            return
        if jj % 1234 == 0:
            print("YES")
            return

print("NO")
