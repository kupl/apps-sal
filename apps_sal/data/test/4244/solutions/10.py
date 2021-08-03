N = int(input())
A = [int(x) for x in input().split()]
count = 0
for j in range(len(A)):
    count += pow(A[j] - round(sum(A) / len(A)), 2)
print(count)
