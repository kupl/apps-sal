N = input()
good_ints = (str(i) * 3 for i in range(9 + 1))
answer = ''

for good_int in good_ints:
    if good_int in N:
        answer = 'Yes'
        break

print(answer if answer else 'No')
