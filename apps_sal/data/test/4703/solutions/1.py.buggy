s = input()
L = []
sigma = 0


def sprit_sum(string, sprit, num):
    nonlocal sigma
    for i in range(1, len(string) + num - sprit):
        str_front = string[:i]
        str_back = string[i:]
        L.append(int(str_front))
        if num < sprit:
            sprit_sum(str_back, sprit, num + 1)
        else:
            L.append(int(str_back))
            for x in L:
                sigma += x
            L.pop()
        L.pop()


for j in range(len(s)):
    sprit_sum(s, j + 1, 1)
sigma += int(s)
print(sigma)
