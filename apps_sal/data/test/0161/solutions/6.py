def allOnes(x):
    if x.count('1') == len(x):
        return True
    return False


def main():
    x = int(input())
    ans = []
    ops = 0
    xb = bin(x)[2:]
    while True:
        index = -1
        for i in range(len(xb)):
            if xb[i] == '0':
                index = i
                break
        if index == -1:
            break
        index = len(xb) - index
        ans.append(index)
        x = 2 ** index - 1 ^ x
        if allOnes(bin(x)[2:]):
            ops += 1
            break
        x += 1
        xb = bin(x)[2:]
        ops += 2
    print(ops)
    for i in ans:
        print(i, end=' ')


main()
