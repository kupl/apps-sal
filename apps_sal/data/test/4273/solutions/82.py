N = int(input())
S = [input() for i in range(N)]
MARCH_dic = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
MARCH_list = ['M', 'A', 'R', 'C', 'H']
for i in range(N):
    if S[i][0] in MARCH_list:
        MARCH_dic[S[i][0]] += 1
p_01 = MARCH_dic['M'] * MARCH_dic['A'] * MARCH_dic['R']
p_02 = MARCH_dic['M'] * MARCH_dic['A'] * MARCH_dic['C']
p_03 = MARCH_dic['M'] * MARCH_dic['A'] * MARCH_dic['H']
p_04 = MARCH_dic['M'] * MARCH_dic['R'] * MARCH_dic['C']
p_05 = MARCH_dic['M'] * MARCH_dic['R'] * MARCH_dic['H']
p_06 = MARCH_dic['M'] * MARCH_dic['C'] * MARCH_dic['H']
p_07 = MARCH_dic['A'] * MARCH_dic['R'] * MARCH_dic['C']
p_08 = MARCH_dic['A'] * MARCH_dic['R'] * MARCH_dic['H']
p_09 = MARCH_dic['A'] * MARCH_dic['C'] * MARCH_dic['H']
p_10 = MARCH_dic['R'] * MARCH_dic['C'] * MARCH_dic['H']
ans = 0
for i in range(10):
    ans += eval(f'p_{str(i + 1).zfill(2)}')
print(ans)
