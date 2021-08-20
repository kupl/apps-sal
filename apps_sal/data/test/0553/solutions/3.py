count = int(input())
if count == 1:
    print('6')
else:
    hamming = 6
    codes = []
    for _ in range(count):
        new_code = input()
        for code in codes:
            distance = 0
            distance += 0 if new_code[0] == code[0] else 1
            distance += 0 if new_code[1] == code[1] else 1
            distance += 0 if new_code[2] == code[2] else 1
            distance += 0 if new_code[3] == code[3] else 1
            distance += 0 if new_code[4] == code[4] else 1
            distance += 0 if new_code[5] == code[5] else 1
            hamming = min(hamming, distance)
        codes.append(new_code)
    print(int(hamming / 2 - 0.5))
