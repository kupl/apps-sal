n = int(input())
a = list(map(int, input().split()))

pair = 0
impair = 0

for i in a:
    if i % 2:
        impair += 1
    else:
        pair += 1

print(min(pair, impair))
