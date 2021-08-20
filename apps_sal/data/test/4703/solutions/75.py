from functools import reduce


def original_sum(X, init):
    goukei = 0
    if len(X) == 0:
        return sum(init)
    else:
        for i in range(len(X)):
            lstm = init.copy()
            num = int(reduce(lambda x, y: x + y, [str(x) for x in X[0:i + 1]]))
            lstm.append(num)
            Y = X[i + 1:len(X)].copy()
            goukei = goukei + original_sum(Y, lstm)
    return goukei


number = list(input())
init = []
print(original_sum(number, init))
