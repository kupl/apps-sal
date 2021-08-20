(parliamentarian_quantity, hight, width) = map(int, input().split())
if parliamentarian_quantity <= hight * width:
    assembly_hall = [[0] * width for row in range(hight)]
    current = 1
    parity = 1 if width % 2 == 0 else 0
    occupied_chairs = 0
    for i in range(hight):
        for j in range(width):
            if occupied_chairs <= parliamentarian_quantity:
                parliamentarian_number = j + 1 + i * width + parity * (i % 2)
                if parliamentarian_number <= parliamentarian_quantity:
                    assembly_hall[i][j] = parliamentarian_number
                    occupied_chairs += 1
                parity = -parity
            else:
                break
    [print(' '.join(map(str, row))) for row in assembly_hall]
else:
    print(-1)
