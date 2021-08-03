queries = int(input())
output = []

for i in range(queries):
    numCount = input()

    if numCount == '4':
        output.append(input())
    else:
        if numCount == '5':
            l = sorted(map(int, input().split()))
            x, y = l[1], l[3]
        else:
            lastNum = b = x = y = 0
            d = 10 ** 12

            for num in sorted(map(int, input().split())):
                if num == lastNum:
                    count += 1

                    if count == 2:
                        a = b
                        b = num

                        if a and b / a < d:
                            d = b / a
                            x = a
                            y = b

                    elif count == 4:
                        x = y = num
                        break

                else:
                    lastNum = num
                    count = 1
        output.append(str(x) + ' ' + str(x) + ' ' + str(y) + ' ' + str(y))
print('\n'.join(output))
