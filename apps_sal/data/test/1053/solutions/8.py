n = int(input())

ans2 = [0]

for i in range(1, 64):
    ans2.append(ans2[i - 1] + ans2[i - 1] + pow(2, i - 1))


def ans(n):
    if n == 0:
        return 0
    else:
        length = n.bit_length() - 1
        if n == pow(2, length):
            return ans2[length]
        else:
            return ans2[length] + ans(n - pow(2, length)) + pow(2, length)


print(ans(n))
