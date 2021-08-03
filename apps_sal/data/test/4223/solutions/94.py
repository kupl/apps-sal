N = int(input())
S = input()
now = 0
num = 0
for char in S:
    if char != now:
        num += 1
        now = char
print(num)
