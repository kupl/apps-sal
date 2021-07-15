N = input()
max_digit = N[0]

min_tmp = ''
max_tmp = ''
for i in range(len(N)):
    min_tmp += max_digit
    max_tmp += str(int(max_digit) + 1)
    
if  int(min_tmp) >= int(N):
    print(min_tmp)
else:
    print(max_tmp)
