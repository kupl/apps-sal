
n = int(input())
A = list(map(int, input().split()))
flag = input()

zero_flag = []
for i in range(n - 1):
    if flag[i] == "0":
        zero_flag.append(i)

for i in range(len(zero_flag)):
    if i == len(zero_flag) - 1:
        if set(A[zero_flag[i] + 1:]) != set(range(zero_flag[i] + 2, n + 1)):
            print("NO")
            quit()
    elif i == 0:
        if set(A[:zero_flag[i] + 1]) != set(range(1, zero_flag[i] + 2)):
            print("NO")
            quit()
    else:
        if set(A[zero_flag[i - 1] + 1:zero_flag[i] + 1]) != set(range(zero_flag[i - 1] + 2, zero_flag[i] + 2)):
            print("NO")
            quit()

print("YES")
