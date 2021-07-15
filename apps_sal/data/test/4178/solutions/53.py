n = int(input())
h = list(map(int,input().split()))
h = h[::-1]
for i in range(n-1):
  if h[i+1] - h[i] == 1:
    h[i+1] -= 1
  elif h[i+1] - h[i] > 1:
    print("No")
    return
print("Yes")
