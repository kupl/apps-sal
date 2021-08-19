values = [*list(map(int, input().split()))]
(n, m) = values
array = [*list(map(int, input().split()))]
ad = 0
result = []
for i in range(m):
    op = [*list(map(int, input().split()))]
    if op[0] == 1:
        index = op[1] - 1
        array[index] = op[2] - ad
    if op[0] == 2:
        ad += op[1]
    if op[0] == 3:
        index = op[1] - 1
        result.append(str(array[index] + ad))
print('\n'.join(result))
