H, A = list(map(int, input().split()))
count = 0

while(H > 0):
    H = H - A
    count = count + 1

print(count)

