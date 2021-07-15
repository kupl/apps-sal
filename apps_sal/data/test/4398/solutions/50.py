n=int(input())
a,b=input().split()
word=""
for i in range(n):
  word += a[i]+b[i]
print(word)
