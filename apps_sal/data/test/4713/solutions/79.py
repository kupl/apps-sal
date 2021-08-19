N = int(input())
S = input()


def ans052(N: int, S: str):
    x = 0
    x_list = [0]
    for i in range(N):
        if S[i] == 'I':
            x += 1
            x_list.append(x)
        elif S[i] == 'D':
            x -= 1
            x_list.append(x)
    x_list.sort()
    return x_list[-1]


print(ans052(N, S))
