alth = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
S = input()
T = input()
heming = 0
first = [-1] * 26
second = [-1] * 26
first_second = [-1] * 676
for i in range(n):
    if S[i] != T[i]:
        heming += 1
        temp = alth.find(S[i])
        temp2 = alth.find(T[i])
        first[temp] = i
        second[temp2] = i
        first_second[temp * 26 + temp2] = i
error_1 = 0
error_2 = 0
for i in range(676):
    temp = i % 26
    temp2 = i // 26
    if first_second[i] != -1 and first_second[temp * 26 + temp2] != -1:
        error_1 = 1
        print(heming - 2)
        print(first_second[i] + 1, first_second[temp * 26 + temp2] + 1)
        break
if error_1 == 0:
    for i in range(26):
        if first[i] != -1 and second[i] != -1:
            error_2 = 2
            print(heming - 1)
            print(first[i] + 1, second[i] + 1)
            break
    if error_2 == 0:
        print(heming)
        print(-1, -1)
