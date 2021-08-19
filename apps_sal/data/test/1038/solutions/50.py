def main():
    (A, B) = list(map(int, input().split()))
    if A == B:
        return A
    elif A % 2 == 0 and B % 2 == 0:
        tmp = int((B - A) / 2)
        if tmp % 2 == 0:
            return 0 ^ B
        else:
            return 1 ^ B
    elif A % 2 == 0 and B % 2 == 1:
        tmp = int((B - A + 1) / 2)
        if tmp % 2 == 0:
            return 0
        else:
            return 1
    elif A % 2 == 1 and B % 2 == 0:
        tmp = int((B - A - 1) / 2)
        if tmp % 2 == 0:
            return 0 ^ B ^ A
        else:
            return 1 ^ B ^ A
    elif A % 2 == 1 and B % 2 == 1:
        tmp = int((B - A) / 2)
        if tmp % 2 == 0:
            return 0 ^ A
        else:
            return 1 ^ A


print(main())
