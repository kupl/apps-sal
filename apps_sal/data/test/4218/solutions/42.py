user_input = int(input())
count = 0
for i in range(0, user_input + 1):
    if i % 2 != 0:
        count += 1
final_result = count / user_input
print('%.10f' % final_result)
