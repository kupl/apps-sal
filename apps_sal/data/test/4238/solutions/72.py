N = input()


def ans176(N: str):
    sum = 0
    for i in range(len(str(N))):
        sum += int(str(N)[i])
    if sum % 9 == 0:
        return("Yes")
    else:
        return("No")


print(ans176(N))
