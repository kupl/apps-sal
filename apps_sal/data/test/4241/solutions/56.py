import numpy as np

def __starting_point():

    s = input()
    t = input()
    
    min_diff = 9999
    len_s = len(s)
    len_t = len(t)
    for i in range(len_s - len_t +1):
        count = 0
        for j in range(len_t):
            if t[j] is not s[i+j]:
                count += 1
        min_diff = min(count, min_diff)

    print(min_diff)
__starting_point()
