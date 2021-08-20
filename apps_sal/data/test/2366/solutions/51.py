N = int(input())
Alst = list(map(int, input().split()))
Blst = [0] * (N + 1)
num = 0
for i in Alst:
    num = num + Blst[i]
    Blst[i] += 1
for i in Alst:
    k = Blst[i] - 1
    print(num - k)
