
def task(a, b, n):
    # check hall capacity
    if n > (a * b):
        print(-1)
        return

    guest_d = 1  # dem guest
    guest_r = 2  # rep guest

    for i in range(a):
        line = ""
        # check row index
        if i % 2 == 0:
            # democrats go first
            for j in range(b):
                # check seat index
                if j % 2 == 0:
                    if guest_d > n:
                        guest_d = 0  # no more democrats

                    if guest_d == 0:
                        line += "0 "
                        continue

                    line += str(guest_d) + " "
                    guest_d += 2

                else:
                    if guest_r > n:
                        guest_r = 0  # no more republicans

                    if guest_r == 0:
                        line += "0 "
                        continue

                    line += str(guest_r) + " "
                    guest_r += 2

        else:
            # republicans go first
            for j in range(b):
                # check seat index
                if j % 2 == 0:
                    if guest_r > n:
                        guest_r = 0  # no more republicans

                    if guest_r == 0:
                        line += "0 "
                        continue

                    line += str(guest_r) + " "
                    guest_r += 2

                else:
                    if guest_d > n:
                        guest_d = 0  # no more democrats

                    if guest_d == 0:
                        line += "0 "
                        continue

                    line += str(guest_d) + " "
                    guest_d += 2

        print(line)


def main():
    # read program args
    line = input().split(" ")
    n = int(line[0])
    a = int(line[1])
    b = int(line[2])

    # list of guests
    task(a, b, n)


main()
