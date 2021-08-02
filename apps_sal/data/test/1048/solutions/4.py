n = int(input())
a = input()
l = [a.count('L'), a.count('R'), a.count('D'), a.count('U')]
print(min(l[0], l[1]) * 2 + min(l[2], l[3]) * 2)
