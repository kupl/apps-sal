A, B, C, D = int(input()), int(input()), int(input()), int(input())
print(((A ^ B) and (C or D)) ^ ((B and C) or (A ^ D)))


