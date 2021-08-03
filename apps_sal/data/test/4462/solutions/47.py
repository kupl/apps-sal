from collections import Counter

n = int(input())
A = list(map(int, input().split()))
A = [min(x & -x, 4) for x in A]

CA = Counter(A)
num0 = CA[1]
num1 = CA[2]
num2 = CA[4]
if num1:
    num1 = 1
if num2 - (num1 + num0) >= -1:
    print("Yes")

else:
    print("No")
