def solution():
    string = input()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    now = "a"
    res = 0
    for i in range(len(string)):
        d = abs(alphabet.find(now) - alphabet.find(string[i]))
        res += min(d, 26 - d)
        now = string[i]
    print(res)

solution()

