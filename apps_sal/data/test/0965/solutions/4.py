n = int(input())
s = input()
(a, i) = (s.count('A'), s.count('I'))
print((a, 1, 0)[min(i, 2)])
