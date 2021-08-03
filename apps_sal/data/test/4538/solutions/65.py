def test():
    ans3 = 0
    input_ex = input()
    input_ex1 = input_ex.split()
    n = int(input_ex1[0])
    d = int(input_ex1[1])
    for i in range(0, n):
        input_exa = input()
        input_ex2 = input_exa.split()
        a = int(input_ex2[0])
        b = int(input_ex2[1])
        ans = (a**2 + b**2)
        ans_2 = ans**0.5
        if ans_2 > d:
            pass
        else:
            ans3 += 1
    print(ans3)


test()
