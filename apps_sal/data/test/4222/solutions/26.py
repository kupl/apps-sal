N, K = list(map(int, input().split()))

table = [0] * N
for _ in range(K):
    num = int(input())
    have_list = list(map(int, input().split()))
    for child in have_list:
        table[child - 1] += 1

print(str(table.count(0)))
