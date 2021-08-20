N = int(input())
S = list(input())
x = 0
max = 0
for i in range(N):
    if S[i] == 'I':
        x += 1
    else:
        x -= 1
    if x > max:
        max = x
print(max)
