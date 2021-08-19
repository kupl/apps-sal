S = input()
count1 = S[::2].count('0') + S[1::2].count('1')
count2 = len(S) - count1
print(min(count1, count2))
