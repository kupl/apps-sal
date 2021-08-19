(A, B) = list(map(int, input().split()))
i_num = 100


def get_one(N, i_num=i_num):
    n_list = [0] * i_num
    for i in range(i_num):
        N_ = N
        if 2 ** i > N_:
            break
        if N_ // 2 ** i % 2 == 0:
            N_ = 2 ** i * (N // 2 ** i) - 1
        n_list[i] = (N_ // 2 ** i - 1) // 2 * 2 ** i + N_ % 2 ** i + 1
    return n_list


B_ = get_one(B)
A_ = get_one(A - 1)
ans_ = [0] * i_num
for i in range(i_num):
    if (B_[i] - A_[i]) % 2 != 0:
        ans_[i] = 1
ans_.reverse()
ans = ''.join(map(str, ans_))
print(int(ans, 2))
