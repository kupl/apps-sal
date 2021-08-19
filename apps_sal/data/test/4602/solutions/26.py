n = int(input())
k = int(input())
x = [int(s) for s in input().split()]
move = 0
for i in x:
    move += min(i, abs(i - k)) * 2
print(move)
