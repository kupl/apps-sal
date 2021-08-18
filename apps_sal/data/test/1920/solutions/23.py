n = int(input())
days = [[0, 0] for i in range(366)]
for i in range(n):
    str_input = list(input().split())
    row = 0
    if str_input[0][0] == 'M':
        row = 1
    for j in range(int(str_input[1]) - 1, int(str_input[2])):
        days[j][row] += 1
cnt_guests = 0
for i in range(366):
    cnt_guests = max(cnt_guests, min(days[i][0], days[i][1]) * 2)
print(cnt_guests)
