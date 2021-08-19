def works(numbers):
    if numbers[1] or numbers[2] or numbers[3]:
        if numbers[7] or numbers[0] or numbers[9]:
            if numbers[1] or numbers[4] or numbers[7] or numbers[0]:
                if numbers[3] or numbers[6] or numbers[9] or numbers[0]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


n = int(input())
line = input()
numbers = {}
for i in range(10):
    numbers[i] = False
for ch in line:
    numbers[int(ch)] = True
if works(numbers):
    print('YES')
else:
    print('NO')
