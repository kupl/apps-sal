lst = input().split()
N = int(lst[0])
X = int(lst[1])
lst = []
for i in range(N):
   lst.append(int(input()))

count = N
X -= sum(lst)

count += (X // min(lst))

print(count)
