n = int(input())
s = input()

print(min([s.count('L'), s.count('R')]) * 2 + min([s.count('D'), s.count('U')]) * 2)
