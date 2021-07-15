n = int(input())
sizes = list(map(int, input().strip().split()))
count = [0 for i in range(200002)]
for i in range(n):
    for j in range(i+1,n):
        count[sizes[i] + sizes[j]] += 1
mx = 0
for i in count:
    mx = max(mx,i)
print(mx)
