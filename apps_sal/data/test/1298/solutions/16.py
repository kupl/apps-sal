n = int(input())
s = input()
s = list(map(int, s))
print(abs(s.count(1) - s.count(0)))
