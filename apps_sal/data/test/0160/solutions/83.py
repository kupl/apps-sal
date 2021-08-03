# 約数の列挙
#############################################################


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
#############################################################


N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

sum_A = sum(A)
div_list = make_divisors(sum_A)
ans = 1
# print(div_list)

for div in div_list:
    tmp = []
    for a in A:
        tmp.append(a % div)
    tmp.sort()
    cumsum1 = [0]
    cumsum2 = [0]
    for i in tmp:
        cumsum1.append(cumsum1[-1] + i)
        if i != 0:
            cumsum2.append(cumsum2[-1] + (div - i))
        else:
            cumsum2.append(cumsum2[-1])
    for i in range(1, N):
        if cumsum1[i] <= K and cumsum2[N] - cumsum2[i] <= K:
            ans = div

print(ans)
