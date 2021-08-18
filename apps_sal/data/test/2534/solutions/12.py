from sys import stdin, stdout

r, c = map(int, stdin.readline().strip().split())
gift_list = [list(map(int, stdin.readline().strip().split())) for _ in range(r)]

max_list = [max(i) for i in zip(*gift_list)]
found = False
for i in range(r):
    min_row = min(gift_list[i])
    for j in range(c):
        if gift_list[i][j] == min_row and gift_list[i][j] == max_list[j]:
            print(gift_list[i][j])
            found = True
            break
    if found:
        break
else:
    print("GUESS")
