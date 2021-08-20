N = int(input())
A = list(map(int, input().split()))
ans_lis = [0]
check = False
count = 0
for i in range(N - 1):
    if check == True and A[i] < A[i + 1] or i == N - 2:
        if A[i] >= A[i + 1]:
            count += 1
        ans_lis.append(count)
        check = True
        count = 0
    elif check == False and A[i] >= A[i + 1]:
        check = True
        count = 1
    elif check == True and A[i] >= A[i + 1]:
        count += 1
print(max(ans_lis))
