(code_number, characteristic_code, integer3) = map(int, input().split())
integer2 = list(map(int, input().split()))
integer1 = [list(map(int, input().split())) for i in range(code_number)]
solution = 0
for i in range(code_number):
    multiplication = integer3
    for j in range(characteristic_code):
        multiplication += integer2[j] * integer1[i][j]
    if multiplication > 0:
        solution += 1
print(solution)
