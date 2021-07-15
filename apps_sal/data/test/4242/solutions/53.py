def __starting_point():
    A, B, K = list(map(int, input().split()))
    a_ans = []
    b_ans = []
    for a in range(1, A+1):
        if A%a == 0:
            a_ans.append(a)
    for b in range(1, B+1):
        if B%b == 0:
            b_ans.append(b)
    ans = list(set(a_ans) & set(b_ans))
    ans.sort(reverse=True)

    print((ans[K-1]))

__starting_point()
