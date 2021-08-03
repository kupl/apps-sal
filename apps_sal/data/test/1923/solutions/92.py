n = int(input())
l = list(map(int, input().split()))
l.sort()
kusi = 0
for i in range(n):
    kusi += l[i * 2]
print(kusi)
