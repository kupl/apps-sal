n = int(input())
x = 0
for i in range(n):
    S = input()
    if S.count('++'):
        x += 1
    else:
        x -= 1
print(x)
