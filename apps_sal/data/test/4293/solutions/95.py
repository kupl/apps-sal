(P, Q, R) = map(int, input().split())
time = [P + Q, P + R, R + Q]
time.sort()
print(time[0])
