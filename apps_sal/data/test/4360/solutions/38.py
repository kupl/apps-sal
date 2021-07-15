N = int(input())
A = list(map(int, input().split()))

tmp = 0
for i in A:
    tmp += 1/i
print(1/tmp)
