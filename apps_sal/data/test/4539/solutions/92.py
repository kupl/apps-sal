N = input()
N_int = int(N)
N_len = len(N)
N_wa = 0
for i in range(N_len):
    N_wa += int(N[i])
if N_int % N_wa == 0:
    print('Yes')
else:
    print('No')
