n = int(input())
flag = False
a = list(map(int, input().split()))
for i in a:
    if i == 1:
        flag = True
if flag:
    print("HARD")
else:
    print("EASY")
