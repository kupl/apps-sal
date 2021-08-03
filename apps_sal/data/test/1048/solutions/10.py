n = int(input())
s = input()
k = 2 * (min(s.count('U'), s.count('D')) + min(s.count('L'), s.count('R')))
print(k)
