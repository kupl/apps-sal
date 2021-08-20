K = int(input())


def digit_sum(s):
    return sum([int(i) for i in str(s)])


def f(n):
    n = str(n)
    (f_min, f_ans) = (float('inf'), -1)
    for i in range(len(n)):
        for x in range(int(n[i]), 10):
            s = n[:i] + str(x) + '9' * (len(n) - i - 1)
            if f_min > int(s) / digit_sum(s):
                f_min = int(s) / digit_sum(s)
                f_ans = int(s)
    return f_ans


ans = [1]
for k in range(K - 1):
    ans.append(f(ans[-1] + 1))
print(*ans, sep='\n')
