N = int(input())
A_l = map(int, input().split())
M = 0
B = 0
for i in A_l:
    if i >= M:
        B += 0
        M = i
    else:
        B += M - i
print(B)
