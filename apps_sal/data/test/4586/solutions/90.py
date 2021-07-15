N = input()
good_ints = (str(i) * 3 for i in range(9 + 1))

for good_int in good_ints:
    if good_int in N:
        print('Yes')
        return

print('No')
