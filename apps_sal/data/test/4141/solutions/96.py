N = int(input())
num = list(map(int, input().split()))
even = []
for i in range(N):
    if num[i] % 2 == 0:
        even.append(num[i])
for j in range(len(even)):
    if (even[j] % 5 != 0) and (even[j] % 3 != 0):
        print("DENIED")
        return
print("APPROVED")
