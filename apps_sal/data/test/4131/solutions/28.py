n, m = map(int, input().split())
numbers = [{} for _ in range(n)]

for i in range(m):
    p, y = map(int, input().split())
    numbers[p - 1][i] = y  # pで県を指定して、iで順番の情報を保つ

answers = {}

for i in range(n):
    number = numbers[i]
    if len(number) == 0:
        continue
    new_number = sorted(number.items(), key=lambda x: x[1])  # x[1]で誕生ねんでソート
    cnt = 1
    for num in new_number:
        answers[num[0]] = (6 - len(str(i + 1))) * '0' + str(i + 1) + (6 - len(str(cnt))) * '0' + str(cnt)
        cnt += 1

answer = sorted(answers.items(), key=lambda x: x[0])

for i in answer:
    print(i[1])
