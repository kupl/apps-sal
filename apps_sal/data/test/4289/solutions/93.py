N = input()
T, A = map(int, input().split())
H = list(map(int, input().split()))
min = 100000
count = 1
num = 0

for h in H:
    titen = T - h * 0.006
    s = abs(A - titen)
    if s < min:
        min = s
        num = count
    count += 1

print(num)
