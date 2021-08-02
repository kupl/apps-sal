n = int(input())

sum = 0
line = input().split()

freq = [];
for i in range(0, 11):
    freq.append(0);
for item in line:
    freq[len(item)] += 1


def solve1(str, l):
    n = len(str)
    i = 0
    s = ""
    if n >= l:
        s = str[0:n - l]
        i = n - l
    for k in range(i, n):
        s = s + str[k] + "0"
    return s


def solve2(str, l):
    n = len(str)
    i = 0
    s = ""
    if n >= l:
        s = str[0:n - l]
        i = n - l
    for k in range(i, n):
        s = s + "0" + str[k]
    return s


for i in range(0, n):
    for l in range(1, 11):
        if freq[l] != 0:
            temp1 = solve1(line[i], l)
            temp2 = solve2(line[i], l)
            sum = sum + (int(temp1) + int(temp2)) * freq[l]
            sum %= 998244353

print(sum)
