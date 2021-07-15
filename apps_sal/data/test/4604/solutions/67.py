import sys

# n = 10 ** 5
# データ読み込み関係
n = int(input())

a = list(map(int, input().split(' ')))

record = {}

possible = True

# 状況が実現可能か確認
for e in a:
    if(e in record.keys()):
        record[e] += 1
        if(record[e] == 2):
            if(e == 0):
                possible = False
                break
        if(record[e] == 3):
            possible = False
            break
    else:
        record[e] = 1

if(possible == False):
    print(0)
    return

multiCount = int(n / 2)

print(2 ** multiCount % (10 ** 9 + 7))
