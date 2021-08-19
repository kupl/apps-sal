lst = input().split()
N = int(lst[0])
A = int(lst[1])
B = int(lst[2])


def sum(n):
    result = 0
    s = str(n)
    for i in range(len(s)):
        result += int(s[i])
    return result


count = 0
for i in range(1, N + 1):
    if A <= sum(i) <= B:
        count += i
print(count)
