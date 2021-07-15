H, A = map(int, input().split())
count=0
while(H > 0):
    H -= A
    count += 1
print(count)
