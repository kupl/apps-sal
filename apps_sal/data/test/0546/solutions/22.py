def local_right_to_global(test, local_right):
    return(len(test) + local_right)
    
def local_left_to_global(test, local_left):
    return(local_left)

def check_left(test, template, good_symbols):
    left_idx = -1
    for symbol in template:
        left_idx += 1
        if symbol == '*':
            return(local_left_to_global(test, left_idx))
        try:
            if test[left_idx] != template[left_idx]:
                if template[left_idx] != '?':
                    return('NO')
                elif test[left_idx] not in good_symbols:
                    return('NO')
        except:
            return('NO')

def check_right(test, template, good_symbols):
    right_idx = 0
    for symbol in reversed(template):
        right_idx -= 1
        if symbol == '*':
            return(local_right_to_global(test, right_idx))
        try:
            if test[right_idx] != template[right_idx]:
                if template[right_idx] != '?':
                    return('NO')
                elif test[right_idx] not in good_symbols:
                    return('NO')            
        except:
            return('NO')
    
good_symbols = set(list(input()))
template = input()
tests_nr = int(input())
tests = []
for _ in range(tests_nr):
    tests.append(input())
    
abaca = '*' not in template
for test in tests:
    if abaca:
        pos = -1
        flag = True
        if len(test) != len(template):
            print('NO')
            continue
        for symbol in template:
            pos += 1
            try:
                if test[pos] != template[pos]:
                    if template[pos] != '?':
                        print('NO')
                        flag = False
                        break
                    elif test[pos] not in good_symbols:
                        print('NO')
                        flag = False
                        break
            except:
                print('NO')
                flag = False
                break
        if flag:
            print('YES')
        continue
    left_idx = check_left(test, template, good_symbols)
    right_idx = check_right(test, template, good_symbols)
    # print(left_idx, right_idx)
    if left_idx == 'NO':
        print('NO')
    elif right_idx == 'NO':
        print('NO')
    else:
        if right_idx < left_idx - 1:
            print('NO')
            continue
        flag = True
        for pos in range(left_idx, right_idx + 1):
            if test[pos] in good_symbols:
                print('NO')
                flag = False
                break
        if flag:
            print('YES')

