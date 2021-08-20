N = int(input())


def can():
    judge = 'No'
    for i in range(1, 10):
        if int(N / i) < 10 and N % i == 0:
            judge = 'Yes'
            break
    return judge


print(can())
