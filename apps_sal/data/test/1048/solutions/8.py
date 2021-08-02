n = int(input())
s = input()

count = min(s.count('U'), s.count('D')) + min(s.count('L'), s.count('R'))
print(count * 2)
