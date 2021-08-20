n = int(input())
s = input()
print(*[chr(65 + (ord(i) + n - 65) % 26) for i in s], sep='')
