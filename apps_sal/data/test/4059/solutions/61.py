N = int(input())
count = 0

for a in range(1, N):
    count +=int((N-1)/a)

print(count)
