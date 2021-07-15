n = input()
digit_sum = 0
for i in range(len(n)):
    digit_sum += int(n[i])
print('Yes') if int(n) % digit_sum == 0 else print('No')
