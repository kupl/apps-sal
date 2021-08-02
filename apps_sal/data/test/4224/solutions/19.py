N = int(input())
A = list(map(int, input().split()))
list1 = []
for i in range(N):
    cnt = 0
    if A[i] % 2 == 1:
        continue
    else:
        while A[i] % 2 == 0:
            cnt += 1
            A[i] = A[i] // 2
        list1.append(cnt)

if list1 == []:
    print(0)
elif len(list1) == 1:
    print(list1[0])
else:
    print(sum(list1))
