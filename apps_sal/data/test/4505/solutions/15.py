# A - abc of ABC

# 標準入力S
S = input()
abc_list = ["a", "b", "c"]

for i in S:
    if i in abc_list:
        abc_list.remove(i)

if len(abc_list) == 0:
    print('Yes')
else:
    print('No')
    


