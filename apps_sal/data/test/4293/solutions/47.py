A, B, C = map(int, input().split())

list = [A + B, B + C, A + C]
new_list = sorted(list)

print(new_list[0])
