N = int(input())


def minus_binary(n, S: str):
    if n == 0:
        if S == "":
            S = "0"
        return S

    if n == 1:
        S = "1" + S
        return minus_binary(0, S)

    else:
        if n % 2 == 1:
            n -= 1
            S = "1" + S
        else:
            S = "0" + S

        return minus_binary(n / (-2), S)


S = ""
print(minus_binary(N, S))
