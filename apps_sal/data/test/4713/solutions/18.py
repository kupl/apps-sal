N = int(input())
S = input()

max_num = 0
idx = 0
x = 0
while idx < N:
    if S[idx] == 'I':
        x += 1
    else:
        x -= 1
    max_num = max(x, max_num)
    idx += 1

print(max_num)
