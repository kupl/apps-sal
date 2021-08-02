S = input()

min_num = 753
for i in range(len(S) - 2):
    diff = abs(753 - int(S[i:i + 3]))
    min_num = diff if diff < min_num else min_num

print(min_num)
