import copy
n, k = [int(x) for x in input().split()]
s = input()
for i in range(k):
    t = []
    if n % 2 == 1:
        n *= 2
        s = s * 2
    for j in range(int(n / 2)):
        if (s[2 * j] == "R" and s[2 * j + 1] == "S") or (s[2 * j] == "S" and s[2 * j + 1] == "R"):
            t.append("R")
        elif (s[2 * j] == "R" and s[2 * j + 1] == "P") or (s[2 * j] == "P" and s[2 * j + 1] == "R"):
            t.append("P")
        elif (s[2 * j] == "S" and s[2 * j + 1] == "P") or (s[2 * j] == "P" and s[2 * j + 1] == "S"):
            t.append("S")
        else:
            t.append(s[2 * j])
    n /= 2
    s = copy.deepcopy(t)
    # print(s)
print(s[0])
