(a, b, c) = list(map(int, input().split()))
(e, f, g) = list(map(int, input().split()))
(h, i, j) = list(map(int, input().split()))
bingo_list = [[a, b, c], [e, f, g], [h, i, j], [a, e, h], [b, f, i], [c, g, j], [a, f, j], [c, f, h]]
n = int(input())
n_list = [int(input()) for _ in range(n)]
count = 0
ans = 'No'
for i in bingo_list:
    for j in n_list:
        if j in i:
            count += 1
        if count == 3:
            ans = 'Yes'
            break
    if ans == 'Yes':
        break
    count = 0
print(ans)
