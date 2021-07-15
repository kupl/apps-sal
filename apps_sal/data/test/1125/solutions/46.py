def digit(x):
    ret = 0
    while x > 0:
        x //= 2
        ret += 1
    return ret

def main():
    N = int(input())
    A = list(map(int, input().split()))
    g = 0
    for i in range(2, N):
        g ^= A[i]
    a0 = A[0]
    a1 = A[1]
    ans = 0
    half = 2**20
    if a0 < half:
        for i in range(a0):
            t0 = a0 - i
            t1 = a1 + i
            if t0 ^ t1 == g:
                print(i)
                return
        print((-1))
        return

    # check upper part (2**20 <= x)
    ug = g >> 20
    b0 = a0 >> 20
    b1 = a1 >> 20
    upper_ans_0 = -1 # a0: no borrow, a1: no carry
    for i in range(b0):
        t0 = b0 - i
        t1 = b1 + i
        if t0 ^ t1 == ug:
            upper_ans_0 = i
            break

    upper_ans_1 = -1 # a0: no borrow, a1: carry
    for i in range(b0):
        t0 = b0 - i
        t1 = b1 + 1 + i
        if t0 ^ t1 == ug:
            upper_ans_1 = i
            break

    upper_ans_2 = -1 # a0: borrow, a1: no carry
    for i in range(b0-1):
        t0 = b0 - 1 - i
        t1 = b1 + i
        if t0 ^ t1 == ug:
            upper_ans_2 = i
            break

    upper_ans_3 = -1 # a0: borrow, a1: carry
    for i in range(b0-1):
        t0 = b0 - 1 - i
        t1 = b1 + 1 + i
        if t0 ^ t1 == ug:
            upper_ans_3 = i
            break

    # print(upper_ans_0, upper_ans_1, upper_ans_2, upper_ans_3)
    # check lower part (0 ... 2**20)
    lower_answers = []
    for i in range(half):
        t0 = (a0 - i) % half
        t1 = (a1 + i) % half
        if t0 ^ t1 == (g % half):
            lower_answers.append(i)
    if len(lower_answers) == 0:
        print((-1))
        return
    # print(len(lower_answers))
    # print(lower_answers)
    answers = []
    for l in lower_answers:
        if (a0 % half) >= l:
            # a0: no borrow
            if (a1 % half) + l < half:
                # no carry
                if upper_ans_0 != -1:
                    answers.append((upper_ans_0 << 20) + l)
            else:
                # carry
                if upper_ans_1 != -1:
                    answers.append((upper_ans_1 << 20) + l)
        else:
            # a0: borrow
            if (a1 % half) + l < half:
                # no carry
                if upper_ans_2 != -1:
                    answers.append((upper_ans_2 << 20) + l)
            else:
                # carry
                if upper_ans_3 != -1:
                    answers.append((upper_ans_3 << 20) + l)
    if len(answers) == 0:
        print((-1))
        return
    answers.sort()
    print((answers[0]))

def __starting_point():
    main()

__starting_point()
