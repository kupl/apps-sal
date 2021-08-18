def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if ((n % i == 0)):
            if(i > 1):
                divisors.append(i)
            if i != n // i:
                if(n // i > 1):
                    divisors.append(n // i)
    return divisors


def test(n, ans_list):
    ans_list.append(n)
    ans_list = ans_list + make_divisors(n - 1)

    for ans in make_divisors(n):
        nn = n
        while(nn % ans == 0):
            nn = nn / ans
        nn = nn % ans
        if(nn == 1):
            ans_list.append(ans)
    return ans_list


n = int(input())

ans_list = []

answer = list(set(test(n, ans_list)))

print(len(answer))
