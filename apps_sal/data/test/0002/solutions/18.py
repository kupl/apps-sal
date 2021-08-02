def main():
    NUMBERS = [str(i) for i in range(1, 10)]
    num = input()
    result = ''
    if num in NUMBERS:
        result = 1
        return result
    if len(num) == num.count('0') + 1:
        result = int(str(int(num[0]) + 1) + num[1:]) - int(num)
        return result
    result = int(str(int(num[0]) + 1) + (len(num) - 1) * '0') - int(num)
    return result


print(main())
