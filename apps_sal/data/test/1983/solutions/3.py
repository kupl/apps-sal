a = int(input())
for i in range(a):
    o = int(input())
    u = list(map(int, input().split()))
    print(len(set(u)))
