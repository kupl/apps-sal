A, B = map(int, input().split())

AB_add = A + B
AB_sub = A - B
AB_mul = A * B

AB_list = [AB_add, AB_sub, AB_mul]

print(max(AB_list))
