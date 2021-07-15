import numpy as np


def main():
    S = {i:s for i, s in enumerate(input()[::-1])}
    MOD = 10**9 + 7
    
    DP_table = np.zeros(13).astype(np.int64)
    
    # 初期化
    digit = S[0]
    if digit == '?':
        for i in range(10):
            DP_table[i] = 1
    else:
        DP_table[int(digit)] = 1
        
    transition_matrixes = {}
    for multiplier in range(13):
        for digit in range(10):
            transition_matrix = np.zeros((13, 13)).astype(np.int64)
            for k in range(13):
                transition_matrix[(digit * multiplier + k) % 13, k] = 1
            transition_matrixes[(multiplier, digit)] = transition_matrix

    transition_matrixes2 = {}
    for multiplier in range(13):
        transition_matrixes2[multiplier] = np.zeros((13, 13)).astype(np.int64)
        for digit in range(10):
            transition_matrixes2[multiplier] += transition_matrixes[(multiplier, digit)]
            
    # DP
    multiplier = 1
    for i in range(1, len(S)):
        multiplier = multiplier * 10 % 13
        digit = S[i]
        if digit == '?':
            transition_matrix = transition_matrixes2[multiplier]
        else:
            transition_matrix = transition_matrixes[(multiplier, int(digit))]
        
        DP_table = np.dot(transition_matrix, DP_table)
        DP_table %= MOD

    print((int(DP_table[5])))

    
def __starting_point():
    main()

__starting_point()
