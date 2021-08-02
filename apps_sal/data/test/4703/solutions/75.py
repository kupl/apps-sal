from functools import reduce


def original_sum(X, init):
    goukei = 0
    if(len(X) == 0):
        # print("aaa")
        # print(sum(init))
        return sum(init)
    else:
        for i in range(len(X)):
            lstm = init.copy()
            # print(len(X))
            num = int(reduce(lambda x, y: x + y, [str(x) for x in X[0:i + 1]]))
            # print(num)
            #init = num
            lstm.append(num)
            Y = X[i + 1:len(X)].copy()
            # print(len(Y))
            # if(len(X)-i-1 != 0):
            goukei = goukei + original_sum(Y, lstm)
            # else:
            # sum = sum + (len(X)-i-1)num + original_sum(Y)
            # print(sum)

    return goukei


number = list(input())
init = []
print(original_sum(number, init))
