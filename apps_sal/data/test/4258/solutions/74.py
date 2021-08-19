(A, B, T) = map(int, input().split())
time = A
biscuits = 0
while T + 0.5 >= time:
    biscuits += B
    time += A
print(biscuits)
