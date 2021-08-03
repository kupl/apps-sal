S = list(map(int, list(input())))
first_letter = S[0]
second_letter = 0 if first_letter else 1
res = 0
res += len([i for i in S[0::2] if i != first_letter])
res += len([i for i in S[1::2] if i != second_letter])
print(res)
