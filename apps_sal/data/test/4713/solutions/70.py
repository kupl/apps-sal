N = int(input())
S = input()

m = 0
x = 0
for i in range(N):
    if S[i] == 'I':
        x += 1

    else:
        x -= 1

    m = max(m, x)

print(m)
