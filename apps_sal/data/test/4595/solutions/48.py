s = input()
size = len(s)
for i in range(size):
    if s[i] == 'A':
        head = i
        for j in range(size):
            if s[-1-j] == 'Z':
                tail = j 
                break
        break 
print(size-head-tail)
