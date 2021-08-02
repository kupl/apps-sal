N = int(input())
A = input().split()
num_even = 0
num_approved = 0

for i in range(N):
    if int(A[i]) % 2 == 0:
        num_even += 1
        if int(A[i]) % 3 == 0 or int(A[i]) % 5 == 0:
            num_approved += 1

if num_even == num_approved:
    print("APPROVED")
else:
    print("DENIED")
