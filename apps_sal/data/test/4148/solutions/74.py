n = int(input())
s = input()
ss = [chr(65 + (ord(i) - 65 + n) % 26) for i in s]
print(*ss, sep="")
