n = int(input())
list01 = list(map(int, input().split()))
list02 = []
list03 = []
a = 0
for i in range(n-2):
    list02 = [list01[i], list01[i+1], list01[i+2]]
    list03 = sorted(list02)
    if list02[1] == list03[1]:
        a += 1
print(a)
