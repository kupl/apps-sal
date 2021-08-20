import math
A = input()
B = input()
C = input()
D = input()
E = input()
num = 10
for i in [int(A[-1]), int(B[-1]), int(C[-1]), int(D[-1]), int(E[-1])]:
    if i != 0:
        num = min(num, i)
result = (math.ceil(int(A) / 10) + math.ceil(int(B) / 10) + math.ceil(int(C) / 10) + math.ceil(int(D) / 10) + math.ceil(int(E) / 10)) * 10
if num != 10:
    result = result - 10 + num
print(result)
