# for 文はどこまで含むのか、どこで抜けるのかってこと
N = int(input())
calculation = []

for i in range(1, 10):
    for j in range(1, 10):
        ans = i * j
        calculation.append(ans)

if N in calculation:
    print("Yes")
else:
    print("No")
