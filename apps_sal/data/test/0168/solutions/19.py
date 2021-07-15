x = 10**9+7
N = int(input())
S = input()
mini = x

for s in S:
    if s == '+':
        x += 1
    else:
        x -= 1
    mini = min(mini, x)
print(x - mini)
