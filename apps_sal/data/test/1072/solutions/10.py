__author__ = 'trunghieu11 - vuondenthanhcong11@gmail.com'

# ---------- My Tools -------------

# ------ Input output tools -------
def read_int(): return int(input())
def read_ints(): return map(int, input().split())
def read_list_int(): return list(map(int, input().split()))
def read_strings(row_count):
    answer = []
    for i in range(0, row_count): answer.append(input())
    return answer


# ---------- Actual Code ----------

row_count, column_count = read_ints()
table = read_strings(row_count)

save = set()
answer = 0

for j in range(0, column_count):
    isOk = True
    for i in range(1, row_count):
        if table[i][j] < table[i - 1][j] and ((i - 1) << 15 | i) not in save:
            isOk = False
            answer += 1
            break
    if isOk:
        for i in range(1, row_count):
            if table[i][j] > table[i - 1][j]:
                save.add(((i - 1) << 15 | i))

print(answer)
