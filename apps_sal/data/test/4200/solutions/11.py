n, m = map(int, input().split())
lis = sorted(list(map(int, input().split())), reverse=True)
con = 0

for i in range(n):
    if lis[i] >= sum(lis) * (1 / (4 * m)):
        con += 1
        if con == m:
            print("Yes")
            return

print("No")
