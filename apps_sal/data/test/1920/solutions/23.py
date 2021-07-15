n = int(input())
days = [[0, 0] for i in range(366)]
for i in range(n):
    str_input = list(input().split())
    #print(str_input[0])
    row = 0
    if str_input[0][0] == 'M':
        row = 1
        #print("true")
    #print(int(str_input[1]) - 1, int(str_input[2]))
    for j in range(int(str_input[1]) - 1, int(str_input[2])):
        days[j][row] += 1
cnt_guests = 0
for i in range(366):
    cnt_guests = max(cnt_guests, min(days[i][0], days[i][1]) * 2)
# for i in range(366):
#     print(i + 1, days[i])
print(cnt_guests)

