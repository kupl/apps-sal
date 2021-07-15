def invert(n):
    return str(min(9 - int(n), int(n)))

n = input().strip()
for i in range(len(n)):
    if i == 0 and n[i] == '9':
        print('9', end = '')
        continue
    print(invert(n[i]), end = '')
    
