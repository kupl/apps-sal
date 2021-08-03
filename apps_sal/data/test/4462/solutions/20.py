n = int(input())
a = [int(i) for i in input().split()]

A_num = 0
B_num = 0
C_num = 0

for i in a:
    if i % 4 == 0:
        C_num += 1
    elif i % 2 == 0:
        B_num += 1
    else:
        A_num += 1


def ans():
    if A_num == 1:
        if C_num >= 1:
            return True
        return False
    else:
        if n == 2 * A_num - 1:
            if C_num == A_num - 1:
                return True
            return False

        elif n < 2 * A_num - 1:
            return False
        else:
            if C_num >= A_num:
                return True
            return False


if ans():
    print("Yes")
else:
    print("No")
