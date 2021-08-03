N = int(input())
# b,c=int(input()),int(input())
# c=[]
#  for i in b:
#     c.append(i)
#e1,e2 = map(int,input().split())
A = list(map(int, input().split()))
#j = [input() for _ in range(a)]
# h = []
# for i in range(e1):
#     h.append(list(map(int,input().split())))
A.sort()
ans = "YES"
for i in range(1, N):
    if A[i - 1] == A[i]:
        ans = "NO"
        break
print(ans)
