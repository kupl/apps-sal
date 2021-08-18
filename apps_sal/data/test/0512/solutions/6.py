N = int(input())


def check_AB(A, B):
    if B >= N * 2:
        return False

    if A_table[B] != None:
        return False

    if B_table[A] != None:
        return False

    Ar = B_table[B]
    Br = A_table[A]

    if Ar == -1 and Br == -1:
        return False

    if not(Ar == -1 or Ar == None or Ar == A):
        return False

    if not(Br == -1 or Br == None or Br == B):
        return False

    return True


def check_A2B(A, B):
    if not check_AB(A, B):
        return False
    C = B - A - 1
    for A2 in range(A + 1, B):
        B2 = A2 + C + 1
        if not check_AB(A2, B2):
            return False

    return check(B + C + 1)


def check(A):
    if A >= N * 2:
        return True

    if B_table[A] != None:
        return False

    B = A_table[A]
    if B == None or B == -1:
        B_min = A + 1
        B_max = N * 2
        if not(B_min < B_max):
            return False
    else:
        B_min = B
        B_max = B + 1

    for B in range(B_min, B_max):
        if check_A2B(A, B):
            return True
    return False


A_table = [None] * (2 * N)
B_table = [None] * (2 * N)


def read():
    free_count = 0
    for _ in range(N):
        A, B = list(map(int, input().split()))
        if A >= 1:
            A -= 1
        if B >= 1:
            B -= 1
        if A != -1 and B != -1 and B <= A:
            return False

        if A == -1 and B == -1:
            free_count += 1

        if A != -1:
            if A_table[A] != None or B_table[A] != None:
                return False

        if B != -1:
            if B_table[B] != None or A_table[B] != None:
                return False

        if A != -1:
            A_table[A] = B

        if B != -1:
            B_table[B] = A

    return check(0)


if read():
    print("Yes")
else:
    print("No")
