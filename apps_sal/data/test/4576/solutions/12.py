A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0
# for a in range(A+1):
#     temp = X
#     if temp - 500 * a == 0:
#         count+=1
#         break
#     elif temp - 500 * a > 0:
#         temp -= 500 * a

#     for b in range(B+1):
#         temp_b = temp
#         if b != 0:
#             if temp_b - 100 * b == 0:
#                 count+=1
#                 break
#             elif temp_b - 100 * b > 0:
#                 temp_b -= 100 * b

#         if C > 0:
#             temp_c = temp_b
#             for c in range(1,C+1):
#                 if temp_c - 50 == 0:
#                     count+=1
#                     break
#                 temp_c -= 50
#     if X < 500:
#         break
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            total = 500 * a + 100 * b + 50 * c
            if total == X:
                count+=1

print(count)
