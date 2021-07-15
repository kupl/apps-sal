n = int(input())
ans = 1
for i in input().split():
    if i == '1':
        ans = 0
        break
if ans:
    print("EASY")
else:
    print("HARD")
