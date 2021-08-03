T = int(input())
for t in range(T):
    s = input()
    n = len(s)
    res = 0
    zeros = 0
    for i, c in enumerate(s):
        if c == '0':
            zeros += 1
        else:
            tail = 1
            j = 1
            while tail <= zeros + j:
                res += 1
                j += 1
                if i - 1 + j == n:
                    break
                tail *= 2
                tail += int(s[i - 1 + j])
            zeros = 0
    print(res)
