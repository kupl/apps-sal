x = int(input())
answer_year = 0
deposit = 100
while deposit < x:
    deposit = deposit + deposit // 100
    answer_year += 1
print(answer_year)
