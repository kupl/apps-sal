n = int(input())
print(*[chr(ord(i) + n + [0, -26][ord(i) + n > 90]) for i in input()], sep='')
