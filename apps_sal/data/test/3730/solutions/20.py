from copy import copy

length = int(input())
nums= input().split(" ")
numsList = []

for n in nums:
    numsList.append(int(n))

left = []
right = []

for i in range(length):
    left.append(1)
    right.append(1)
    
for i in range(1, length):
    if numsList[i] > numsList[i-1]:
        left[i] = left[i-1] + 1
    if numsList[length-i] > numsList[length-i-1]:
        right[length-i-1] = right[length-i] + 1

answer = 0
for i in range(length):
    if length == 1:
        answer = 1
    elif i == 0:
        if left[i] == 1:
            maxVal = right[i+1] + left[i] 
            if maxVal > answer:
                answer = maxVal
#         if right[i] == 1:
#             maxVal = right[i+1] + left[i] 
#             if maxVal > answer:
#                 answer = maxVal
    elif i == length-1:
        if left[i] == 1:
            maxVal = left[i-1] + right[i]
            if maxVal > answer:
                answer = maxVal
    else:
        if left[i] == 1:
            if (numsList[i+1] - numsList[i-1] >= 2 or (i-2 > 0 and numsList[i] - numsList[i-2] >= 2)):
                maxVal = left[i-1] + right[i]
                if maxVal > answer:
                    answer = maxVal
            else:
                maxVal = left[i-1] + 1
                if maxVal > answer:
                    answer = maxVal
        if right[i] == 1:
            if (numsList[i+1] - numsList[i-1] >= 2 or (i+2 < length and numsList[i+2] - numsList[i] >= 2)):
                maxVal = right[i+1] + left[i]
                if maxVal > answer:
                    answer = maxVal
            else:
                maxVal = right[i+1] + 1
                if maxVal > answer:
                    answer = maxVal

print (answer)


