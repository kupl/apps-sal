num1 = int(input())
while num1 >= 0:
    if num1 < 1200:
        print(f'ABC')
    elif num1 >= 1200 and num1 < 2800:
        print(f'ARC')
    elif num1 >= 2800 and num1 <= 4208:
        print(f'AGC')
    break
