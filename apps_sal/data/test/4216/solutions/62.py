N = int(input())
minimum = 10**10
for i in range(1,int(N**.5)+1):
    if N%i == 0:
        minimum = min(minimum, max(len(str(i)), len(str(N//i))))
print(minimum)

