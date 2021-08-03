N = int(input())
s = input()


def count(x, y):
    l = []
    result = 0
    for i in range(len(x + y)):
        l.append((x + y)[i])
    for letter in set(l):
        if (letter in x) and (letter in y):
            result += 1
    return result


lst = []
for i in range(1, N):
    lst.append(count(s[:i], s[i:]))

print(max(lst))
