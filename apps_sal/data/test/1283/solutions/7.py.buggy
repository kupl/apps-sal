from pprint import pprint

# if __main__ == ''

N, K = (int(i) for i in input().split())


field = []

count = [[0] * N for i in range(N)]

for i in range(N):
    field.append([c == '.' for c in input()])


for i in range(N):
    for j in range(N):
        # for k in range(K):
        #     print(field[i + k][j])
        if i + K <= N:
            if all(field[i + k][j] for k in range(K)):
                for k in range(K):
                    count[i + k][j] += 1
        if K > 1 and j + K <= N:
            # for k in range(K):
            #     print(field[i][j + k])
            if all(field[i][j + k] for k in range(K)):
                for k in range(K):
                    count[i][j + k] += 1

# print('\n'.join(''.join(str(x) for x in y) for y in count))
# print('\n'.join(''.join('.' if x else '#' for x in y) for y in field))

M = max(max(i) for i in count)

for i in range(N):
    for j in range(N):
        if count[i][j] == M:
            print(i + 1, j + 1)
            return

print(0, 0)
