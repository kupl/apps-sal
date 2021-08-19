(n, x0, y0) = (int(x) for x in input().split())
guys = []
for i in range(n):
    (x, y) = (int(cur) for cur in input().split())
    guys.append((x - x0, y - y0))
answer = 0
while guys:
    (cur_x, cur_y) = guys[0]
    k = 0
    to_remove = []
    for i in range(len(guys)):
        (x, y) = guys[i]
        if x * cur_y == y * cur_x:
            to_remove.append(i - k)
            k += 1
    for index in to_remove:
        del guys[index]
    answer += 1
print(answer)
