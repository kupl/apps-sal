def digsum(n):
    return sum(map(int, str(n)))

A = int(input())
n = A // 2
s = str(n)
s = s[0] + '9' * len(s[1:])
print(digsum(int(s)) + digsum(A-int(s)))
