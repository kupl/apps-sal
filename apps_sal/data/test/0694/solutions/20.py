def main():
    string = input()
    (a, b) = list(map(int, input().split()))
    forward = [-1] * len(string)
    backward = [-1] * len(string)
    x = 1
    for i in range(len(string)):
        cur = int(string[i])
        j = len(string) - i - 1
        curBack = int(string[j])
        if i == 0:
            forward[i] = cur % a
            backward[j] = curBack % b
        else:
            forward[i] = (forward[i - 1] * 10 % a + cur % a) % a
            backward[j] = (backward[j + 1] + curBack * x % b) % b
        x = x * 10 % b
    done = 0
    for i in range(len(string) - 1):
        leftMod = forward[i]
        rightMod = backward[i + 1]
        if leftMod == 0 and rightMod == 0 and (int(string[i + 1]) != 0):
            print('YES')
            print(string[:i + 1])
            print(string[i + 1:])
            done = 1
            break
    if done == 0:
        print('NO')


main()
