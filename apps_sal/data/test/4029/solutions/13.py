import sys
num = input()
length = len(num)
minimum = sys.maxsize
possibles = ["25", "50", "75", "00"]

for possible in possibles:
    if possible[0] == possible[1] and num.count('0') > 1:
        first = num.rfind(possible[0])
        second = num[:first].rfind(possible[1])
        temp_min = length - 2 - second + length - 1 - first
        minimum = min(minimum, temp_min)
    elif possible[0] != possible[1] and possible[0] in num and possible[1] in num:
        first = num.rfind(possible[0])
        second = num.rfind(possible[1])
            
        temp_min = length - 2 - first + length - 1 - second
        
        if (second == 0) and length > 3:
            i = 1
            while num[i] == '0':
                temp_min += 1
                i += 1
        
        if first > second:
            temp_min += 1
        minimum = min(minimum, temp_min)

if minimum == sys.maxsize:
    print(-1)
else:
    print(minimum)
