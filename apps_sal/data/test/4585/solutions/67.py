X = int(input())


def sum_num(x):
    A = [0]
    counter = 0
    for i in range(1, 10**7):
        counter += i
        A.append(counter)
        if A[-2] <= x <= counter:
            return A


print(len(sum_num(X)) - 1)
