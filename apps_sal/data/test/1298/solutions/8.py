def R():
    return list(map(int, input().split()))


input()
s = input()
n = len(s)
n0 = s.count('0')
n1 = s.count('1')
print(max(n - n0 * 2, n - n1 * 2))
