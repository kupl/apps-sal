def task(a, b, n):
    if n > a * b:
        print(-1)
        return
    guest_d = 1
    guest_r = 2
    for i in range(a):
        line = ''
        if i % 2 == 0:
            for j in range(b):
                if j % 2 == 0:
                    if guest_d > n:
                        guest_d = 0
                    if guest_d == 0:
                        line += '0 '
                        continue
                    line += str(guest_d) + ' '
                    guest_d += 2
                else:
                    if guest_r > n:
                        guest_r = 0
                    if guest_r == 0:
                        line += '0 '
                        continue
                    line += str(guest_r) + ' '
                    guest_r += 2
        else:
            for j in range(b):
                if j % 2 == 0:
                    if guest_r > n:
                        guest_r = 0
                    if guest_r == 0:
                        line += '0 '
                        continue
                    line += str(guest_r) + ' '
                    guest_r += 2
                else:
                    if guest_d > n:
                        guest_d = 0
                    if guest_d == 0:
                        line += '0 '
                        continue
                    line += str(guest_d) + ' '
                    guest_d += 2
        print(line)


def main():
    line = input().split(' ')
    n = int(line[0])
    a = int(line[1])
    b = int(line[2])
    task(a, b, n)


main()
