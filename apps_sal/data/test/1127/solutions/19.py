for _ in range(int(input())):
    n = int(input())
    digits = [int(c) for c in input()]
    ans = None
    if n & 1:
        # if n is odd
        for i in range(0, n, 2):
            if digits[i] & 1:
                ans = True
                break
        else:
            ans = False
    else:
        for i in range(1, n, 2):
            if digits[i] % 2 == 0:
                ans = False
                break
        else:
            ans = True

    print(1 if ans else 2)
