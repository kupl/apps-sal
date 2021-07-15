# n = int(input())
# arr = list(map(int, input().split()))
#
# #circle 1
# #triangle 2
# # square 3
# dic = {(1,1): "I", (1,2):3, (1,3):4, (2,1):3, (2,2):"I", (2,3):"I", (3,1):4, (3,2):"I", (3,3):"I"}
#
# c = 0
# for i in range(len(arr)-1):
#     if dic[(arr[i], arr[i+1])] == "I":
#         print("Infinite")
#         return
#     else:
#         c += dic[(arr[i], arr[i+1])]
#
# print("Finite")
# print(c)

n, z = list(map(int, input().split()))

arr = list(map(int, input().split()))



arr.sort()
c = 0
l = 0
r = len(arr)//2
while(r < len(arr) and l < len(arr)):
    # print(arr)
    if arr[l] == -1:
        l += 1
        continue
    if (arr[r] - arr[l]) >= z and arr[r] != -1:
        arr[r] = -1
        c += 1
        r += 1
        l += 1
    else:
        r += 1


print(c)

# from collections import Counter
# n = int(input())
#
#
# for _ in range(n):
#     word = input()
#     nC = [0]*27
#     for i in word:
#         nC[ord(i)%97] += 1
#     wordN = ""+word[0]
#     nC[ord(word[0])%97] -= 1
#     print(nC, wordN)
#     while len(wordN) < len(word):
#         lastidx = ord(wordN[-1])%97
#         flag = True
#         for i in range(len(nC)-1, -1, -1):
#             if i == lastidx+1 or i == lastidx-1:
#                 continue
#             else:
#                 if nC[i] > 0:
#                     wordN += chr(i+97)
#                     nC[i] -= 1
#                     flag = False
#                     break
#         if flag:
#             print("No answer")
#             break
#     print(wordN)
#     if not flag:
#         print(wordN)

