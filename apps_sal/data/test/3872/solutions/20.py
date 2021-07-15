str1 = input()
str2 = input()

saved = {}

def str_equal(str1, str2):
    
    if (str1, str2) in saved:
        return saved[(str1, str2)]
    elif str1 == str2:
        val = True
    elif len(str1) % 2 == 1:
        val = False
    else:
        new_len = len(str1) // 2

        val = ( (str_equal(str1[:new_len], str2[:new_len]) and str_equal(str1[new_len:], str2[new_len:])) or (str_equal(str1[:new_len], str2[new_len:]) and str_equal(str1[new_len:], str2[:new_len])))
    
    saved[(str1, str2)] = val
    return val
    
print('YES' if str_equal(str1, str2) else 'NO')
