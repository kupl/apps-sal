from sys import stdin
N = int(stdin.readline())
num = set()
for b in map(int, stdin.readline().split()):
    while b in num:
        num.remove(b)
        b += 1
    num.add(b)
print(max(num) - len(num) + 1)
