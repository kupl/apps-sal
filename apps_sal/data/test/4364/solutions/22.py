S = input()
num1 = int(S[:2])
num2 = int(S[2:])
if 1 <= num1 <= 12 and 1 <= num2 <= 12:
    ans = 'AMBIGUOUS'
elif 1 <= num1 <= 12 and (num2 == 0 or 12 < num2):
    ans = 'MMYY'
elif (num1 == 0 or 12 < num1) and 1 <= num2 <= 12:
    ans = 'YYMM'
else:
    ans = 'NA'
print(ans)
