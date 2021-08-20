N = int(input())
A = list(map(int, input().split()))
A = [0] + A
Sam = []
Dif = []
D2 = [0] * 200000
for i in range(len(A)):
    Sam.append(i + A[i])
    if i - A[i] > 0:
        Dif.append(i - A[i])
for dif in Dif:
    D2[dif] += 1
count = 0
for sam in Sam:
    if sam < len(D2):
        count += D2[sam]
print(count)
