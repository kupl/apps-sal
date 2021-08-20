S = input()
S_list = list(map(int, S.split()))
S_list = [i - 1 for i in S_list]
if S_list[0] == S_list[1]:
    result = 'Draw'
elif (S_list[0] - S_list[1]) * S_list[1] > 0 or S_list[0] == 0:
    result = 'Alice'
else:
    result = 'Bob'
print(result)
